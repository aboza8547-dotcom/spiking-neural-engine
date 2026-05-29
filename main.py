from complex_cell import ComplexCell
from spiking_cell import SpikingCell
from network import run_with_training


if __name__ == "__main__":

    print("Advanced Spiking Engine")
    print("-" * 40)

    print("\n[1] Complex Numbers")
    z1 = ComplexCell(2, 3)
    z2 = ComplexCell(1, -4)
    print("z1 =", z1)
    print("z2 =", z2)
    print("z1 + z2 =", z1.add(z2))
    print("z1 * z2 =", z1.mul(z2))

    print("\n[2] Training Spiking Neural Network")
    cell_1 = SpikingCell(cell_id=1, threshold=1.0)
    cell_2 = SpikingCell(cell_id=2, threshold=1.0)

    cell_1.connect(cell_2, weight=0.4)
    print("Charging Cell1 with potential = 1.5")
    cell_1.inject(1.5)

    run_with_training([cell_1, cell_2], max_steps=5, learning_rate=0.3)
