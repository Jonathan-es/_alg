import numpy as np

def greedy_param_search(features, targets, start_params=None, max_iter=1000, step_size=0.1):
    """
    Check each parameter with small steps in both directions and update if loss decreases.
    """
    if start_params is None:
        weights = np.zeros(2, dtype=float)
    else:
        weights = np.array(start_params, dtype=float)

    current_loss = mse_loss(features, targets, weights)

    for iteration in range(max_iter):
        any_update = False
        for idx in range(len(weights)):
            for move in [1, -1]:
                trial = weights.copy()
                trial[idx] += move * step_size
                trial_loss = mse_loss(features, targets, trial)
                if trial_loss < current_loss:
                    weights = trial
                    current_loss = trial_loss
                    any_update = True
                    break  # accept first improvement
            if any_update:
                break
        if not any_update:
            step_size *= 0.5  # reduce step for finer search
            if step_size < 1e-6:
                break

    return weights, current_loss
