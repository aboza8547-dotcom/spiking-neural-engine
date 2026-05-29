# ⚡ Advanced Spiking Neural Engine

> A lightweight Python engine combining fractional arithmetic, complex number operations, spiking neural networks with STDP learning, and Riemann zeta approximation.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Components](#components)
- [Example Output](#example-output)
- [Requirements](#requirements)
- [License](#license)

---

## 🧠 Overview

This project implements a biologically-inspired **Spiking Neural Network (SNN)** engine from scratch in pure Python — no external ML frameworks required. It includes:

- Custom numeric cell types (fractional & complex)
- Leaky integrate-and-fire spiking neurons
- **Spike-Timing Dependent Plasticity (STDP)** for online weight training
- Convergence detection for iterative computations
- Riemann zeta function approximation (ζ(2))

---

## ✨ Features

| Feature | Description |
|---|---|
| `FractionalCell` | Wrapper for float arithmetic operations |
| `ComplexCell` | Full complex number support (add, sub, mul, div, magnitude) |
| `SpikingCell` | Spiking neuron with threshold, potential, and spike history |
| `ConvergenceCell` | Monitors value convergence for iterative algorithms |
| STDP Training | Weight update based on relative spike timing between neurons |
| Riemann ζ(2) | Approximates π²/6 via convergence-detected series |

---

## 📁 Project Structure

```
.
└── main.py          # Core engine — all classes and demo in one file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- No external dependencies required (uses only `math` and `dataclasses`)

### Installation

```bash
git clone https://github.com/your-username/advanced-spiking-engine.git
cd advanced-spiking-engine
python main.py
```

---

## 💻 Usage

### Basic Arithmetic

```python
from main import add, sub, mul, div

print(add(2, 3))      # 5
print(div(7, 2))      # 3.5
```

### Complex Numbers

```python
from main import ComplexCell

z1 = ComplexCell(2, 3)   # 2 + 3i
z2 = ComplexCell(1, -4)  # 1 - 4i

print(z1.add(z2))   # 3.000000-1.000000i
print(z1.mul(z2))   # 14.000000-5.000000i
```

### Spiking Neural Network with STDP Training

```python
from main import SpikingCell, run_with_training

cell_1 = SpikingCell(cell_id=1, threshold=1.0)
cell_2 = SpikingCell(cell_id=2, threshold=1.0)

cell_1.connect(cell_2, weight=0.4)  # Connect with initial weak weight
cell_1.inject(1.5)                  # Inject charge to trigger a spike

run_with_training([cell_1, cell_2], max_steps=5, learning_rate=0.3)
```

### Riemann Zeta Approximation

```python
from main import zeta2
import math

print(zeta2(10000))         # ≈ 1.6449
print(math.pi**2 / 6)      # ≈ 1.6449  (expected)
```

---

## 🔬 Components

### `SpikingCell`

Implements a **leaky integrate-and-fire** neuron model:

- `inject(value)` — adds charge to the neuron's membrane potential
- `fire_phase(step)` — fires spikes when potential exceeds threshold; records spike timing
- `propagate_phase(spikes)` — sends spike signals to connected neurons via weighted synapses
- `train_connections(lr)` — applies **STDP rule**: strengthens connections when this cell fires *before* its neighbor; weakens when it fires *after*
- `reset()` — resets potential, spike count, and history

### `ConvergenceCell`

Tracks whether an iterative computation has converged:

- `update(value)` — stores current and previous values
- `converged()` — returns `True` if change is below `epsilon`
- `error()` — returns the absolute difference

---

## 📊 Example Output

```
Advanced Spiking Engine
────────────────────────────────────────

[1] Basic Arithmetic
add(2,3) = 5
sub(2,3) = -1
mul(2.5,4) = 10.0
div(7,2) = 3.5

[2] Complex Numbers
z1 = 2.000000+3.000000i
z2 = 1.000000-4.000000i
z1 + z2 = 3.000000-1.000000i
z1 * z2 = 14.000000-5.000000i

[3] Riemann Approximation
ζ(2) ≈ 1.6449340668482264
Expected π²/6 = 1.6449340668482264

[4] Training Spiking Neural Network
🔋 Charging Cell1 with high potential = 1.5
🚀 Starting network simulation and training (learning rate: 0.3)...
   ↳ Step 0: Cell1 fired a spike! ⚡
🔹 [Training] Strengthened connection: Cell1 -> Cell2 | New weight: 0.70
⏱️ Network stabilized at step 2.
```

---

## 📦 Requirements

```
Python >= 3.8
```

No pip packages needed — pure standard library.

---

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

*Built with pure Python 🐍 — no ML frameworks, no dependencies.*
