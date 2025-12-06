import numpy as np

def calc_gradients(features, targets, weights):
    # weights = [b, m]
    n_samples = features.shape[0]
    predictions = weights[0] + weights[1] * features
    errors = predictions - targets
    grad_b = 2.0 * np.mean(errors)
    grad_m = 2.0 * np.mean(errors * features)
    return np.array([grad_b, grad_m])

def descend_gradient(features, targets, initial_weights=None, lr=0.1, steps=1000, verbose=False):
    weights = np.zeros(2) if initial_weights is None else np.array(initial_weights, dtype=float)
    for step in range(steps):
        grads = calc_gradients(features, targets, weights)
        weights -= lr * grads
        if verbose and (step % (steps // 10 + 1) == 0):
            print(f"step {step}, loss {mse_loss(features, targets, weights):.6f}")
    return weights, mse_loss(features, targets, weights)

def stochastic_grad_desc(features, targets, initial_weights=None, lr=0.01, epochs=50, batch=1, seed=None, verbose=False):
    rng = np.random.RandomState(seed)
    n_samples = features.shape[0]
    weights = np.zeros(2) if initial_weights is None else np.array(initial_weights, dtype=float)
    for ep in range(epochs):
        indices = rng.permutation(n_samples)
        for start in range(0, n_samples, batch):
            batch_idx = indices[start:start+batch]
            Xb, yb = features[batch_idx], targets[batch_idx]
            preds = weights[0] + weights[1] * Xb
            errs = preds - yb
            grad_b = 2.0 * np.mean(errs)
            grad_m = 2.0 * np.mean(errs * Xb)
            weights -= lr * np.array([grad_b, grad_m])
        if verbose and (ep % (epochs // 5 + 1) == 0):
            print(f"epoch {ep}, loss {mse_loss(features, targets, weights):.6f}")
    return weights, mse_loss(features, targets, weights)
