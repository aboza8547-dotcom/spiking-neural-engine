from __future__ import annotations
from dataclasses import dataclass
import math


# ════════════════════════════════════════════════════════════
# Fractional Cell
# ════════════════════════════════════════════════════════════
@dataclass
class FractionalCell:
    value: float = 0.0

    def add(self, other):
        return FractionalCell(self.value + other.value)

    def sub(self, other):
        return FractionalCell(self.value - other.value)

    def mul(self, other):
        return FractionalCell(self.value * other.value)

    def div(self, other):
        if other.value == 0:
            raise ZeroDivisionError()
        return FractionalCell(self.value / other.value)

    def __repr__(self):
        return f"{self.value:.6f}"


# ════════════════════════════════════════════════════════════
# Complex Cell
# ════════════════════════════════════════════════════════════
class ComplexCell:

    def __init__(self, real=0.0, imag=0.0):
        self.real = FractionalCell(real)
        self.imag = FractionalCell(imag)

    def add(self, other):
        return ComplexCell(
            self.real.value + other.real.value,
            self.imag.value + other.imag.value
        )

    def sub(self, other):
        return ComplexCell(
            self.real.value - other.real.value,
            self.imag.value - other.imag.value
        )

    def mul(self, other):
        a = self.real.value
        b = self.imag.value
        c = other.real.value
        d = other.imag.value

        real = (a * c) - (b * d)
        imag = (a * d) + (b * c)

        return ComplexCell(real, imag)

    def div(self, other):
        a = self.real.value
        b = self.imag.value
        c = other.real.value
        d = other.imag.value

        denom = c*c + d*d

        if denom == 0:
            raise ZeroDivisionError()

        real = (a*c + b*d) / denom
        imag = (b*c - a*d) / denom

        return ComplexCell(real, imag)

    def magnitude(self):
        return math.sqrt(
            self.real.value**2 +
            self.imag.value**2
        )

    def __repr__(self):
        r = self.real.value
        i = self.imag.value

        if i >= 0:
            return f"{r:.6f}+{i:.6f}i"
        return f"{r:.6f}{i:.6f}i"


# ════════════════════════════════════════════════════════════
# Advanced Spiking Cell
# ════════════════════════════════════════════════════════════
class SpikingCell:

    def __init__(self, cell_id: int, threshold: float = 1.0):
        self.id = cell_id
        self.threshold = threshold
        self.potential = 0.0
        self.spike_count = 0
        self.connections = []
        self.spike_history = []

    def connect(self, other, weight=1.0):
        self.connections.append([other, weight])

    def inject(self, value):
        self.potential += value

    def fire_phase(self, current_step=0):
        spikes = []
        while abs(self.potential) >= self.threshold:
            if self.potential > 0:
                self.potential -= self.threshold
                spikes.append(+1)
            else:
                self.potential += self.threshold
                spikes.append(-1)

            self.spike_count += 1
            self.spike_history.append(current_step)
        return spikes

    def propagate_phase(self, spikes):
        if len(spikes) == 0:
            return

        for sign in spikes:
            for connection in self.connections:
                neighbor, weight = connection[0], connection[1]
                neighbor.potential += sign * weight

    def train_connections(self, learning_rate=0.1):
        """STDP: strengthen or weaken weights based on relative spike timing"""
        if not self.spike_history:
            return

        last_spike_self = self.spike_history[-1]

        for connection in self.connections:
            neighbor = connection[0]
            if neighbor.spike_history:
                last_spike_neighbor = neighbor.spike_history[-1]

                if last_spike_self < last_spike_neighbor:
                    connection[1] += learning_rate
                    print(f"[Training] Strengthened: Cell{self.id} -> Cell{neighbor.id} | New weight: {connection[1]:.2f}")
                elif last_spike_self > last_spike_neighbor:
                    connection[1] -= learning_rate
                    print(f"[Training] Weakened: Cell{self.id} -> Cell{neighbor.id} | New weight: {connection[1]:.2f}")

    def reset(self):
        self.potential = 0.0
        self.spike_count = 0
        self.spike_history = []

    def __repr__(self):
        return (
            f"Cell{self.id}"
            f"(V={self.potential:.4f}, "
            f"spikes={self.spike_count})"
        )


# ════════════════════════════════════════════════════════════
# Convergence Memory
# ════════════════════════════════════════════════════════════
class ConvergenceCell:

    def __init__(self, epsilon=1e-6):
        self.current = 0.0
        self.previous = 0.0
        self.epsilon = epsilon

    def update(self, value):
        self.previous = self.current
        self.current = value

    def converged(self):
        return abs(self.current - self.previous) < self.epsilon

    def error(self):
        return abs(self.current - self.previous)


# ════════════════════════════════════════════════════════════
# Network Step & Training Engine
# ════════════════════════════════════════════════════════════
def step_and_train(cells, current_step, learning_rate=0.1):
    fired = {}

    for c in cells:
        fired[c.id] = c.fire_phase(current_step=current_step)

    for c in cells:
        c.propagate_phase(fired[c.id])

    for c in cells:
        c.train_connections(learning_rate=learning_rate)

    return fired


def run_with_training(cells, max_steps=100, learning_rate=0.2):
    print(f"\nStarting network simulation (learning rate: {learning_rate})...")
    for s in range(max_steps):
        fired = step_and_train(cells, current_step=s, learning_rate=learning_rate)

        for cell_id, spikes in fired.items():
            if spikes:
                print(f"   Step {s}: Cell{cell_id} fired a spike!")

        all_quiet = all(len(v) == 0 for v in fired.values())
        if all_quiet:
            print(f"Network stabilized at step {s+1}.")
            break


# ════════════════════════════════════════════════════════════
# Arithmetic Operations
# ════════════════════════════════════════════════════════════
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return None if b == 0 else a / b


# ════════════════════════════════════════════════════════════
# Riemann Approximation
# ════════════════════════════════════════════════════════════
def zeta2(iterations=1000):
    conv = ConvergenceCell()
    total = 0.0

    for n in range(1, iterations + 1):
        total += 1 / (n * n)
        conv.update(total)
        if conv.converged():
            break
    return total


# ════════════════════════════════════════════════════════════
# Main Execution
# ════════════════════════════════════════════════════════════
if __name__ == "__main__":

    print("Advanced Spiking Engine")
    print("-" * 40)

    print("\n[1] Basic Arithmetic")
    print("add(2,3) =", add(2, 3))
    print("sub(2,3) =", sub(2, 3))
    print("mul(2.5,4) =", mul(2.5, 4))
    print("div(7,2) =", div(7, 2))

    print("\n[2] Complex Numbers")
    z1 = ComplexCell(2, 3)
    z2 = ComplexCell(1, -4)
    print("z1 =", z1)
    print("z2 =", z2)
    print("z1 + z2 =", z1.add(z2))
    print("z1 * z2 =", z1.mul(z2))

    print("\n[3] Riemann Approximation")
    print("zeta(2) =", zeta2(10000))
    print("Expected pi^2/6 =", math.pi**2 / 6)

    print("\n[4] Training Spiking Neural Network")
    cell_1 = SpikingCell(cell_id=1, threshold=1.0)
    cell_2 = SpikingCell(cell_id=2, threshold=1.0)

    cell_1.connect(cell_2, weight=0.4)
    print("Charging Cell1 with potential = 1.5")
    cell_1.inject(1.5)

    run_with_training([cell_1, cell_2], max_steps=5, learning_rate=0.3)
