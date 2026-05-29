from spiking_cell import SpikingCell


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

        if all(len(v) == 0 for v in fired.values()):
            print(f"Network stabilized at step {s+1}.")
            break
