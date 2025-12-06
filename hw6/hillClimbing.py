import numpy as np

def mse_loss(features, targets, weights):
    # weights = [b, m]
    predictions = weights[0] + weights[1] * features
    return np.mean((predictions - targets) ** 2)

def random_hill_climb(features, targets, start_weights=None, max_iter=5000, step_scale=0.1, seed=None):
    """
    Hill climbing optimization: explore random neighbors and keep improvements.
    step_scale sets the size of random perturbations.
    """
    rng = np.random.RandomState(seed)

    if start_weights is None:
        weights = rng.randn(2)
    else:
        weights = np.array(start_weights, dtype=float)

    best_loss = mse_loss(features, targets, weights)

    for iteration in range(max_iter):
        neighbor = weights + rng.normal(scale=step_scale, size=weights.shape)
        neighbor_loss = mse_loss(features, targets, neighbor)
        if neighbor_loss < best_loss:
            weights, best_loss = neighbor, neighbor_loss

    return weights, best_loss
