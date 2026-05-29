from __future__ import annotations


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
        if not spikes:
            return
        for sign in spikes:
            for connection in self.connections:
                neighbor, weight = connection[0], connection[1]
                neighbor.potential += sign * weight

    def train_connections(self, learning_rate=0.1):
        if not self.spike_history:
            return
        last_spike_self = self.spike_history[-1]
        for connection in self.connections:
            neighbor = connection[0]
            if neighbor.spike_history:
                last_spike_neighbor = neighbor.spike_history[-1]
                if last_spike_self < last_spike_neighbor:
                    connection[1] += learning_rate
                    print(f"[Training] Strengthened: Cell{self.id} -> Cell{neighbor.id} | Weight: {connection[1]:.2f}")
                elif last_spike_self > last_spike_neighbor:
                    connection[1] -= learning_rate
                    print(f"[Training] Weakened: Cell{self.id} -> Cell{neighbor.id} | Weight: {connection[1]:.2f}")

    def reset(self):
        self.potential = 0.0
        self.spike_count = 0
        self.spike_history = []

    def __repr__(self):
        return f"Cell{self.id}(V={self.potential:.4f}, spikes={self.spike_count})"
