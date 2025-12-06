import numpy as np

def gd_with_momentum(features, targets, start_weights=None, lr=0.1, steps=1000, momentum=0.9):
    weights = np.zeros(2) if start_weights is None else np.array(start_weights, dtype=float)
    velocity = np.zeros_like(weights)
    for step in range(steps):
        grad = calc_gradients(features, targets, weights)
        velocity = momentum * velocity + (1 - momentum) * grad
        weights -= lr * velocity
    return weights, mse_loss(features, targets, weights)

def rms_prop(features, targets, start_weights=None, lr=0.01, steps=1000, decay=0.9, eps=1e-8):
    weights = np.zeros(2) if start_weights is None else np.array(start_weights, dtype=float)
    sq_avg = np.zeros_like(weights)
    for step in range(steps):
        grad = calc_gradients(features, targets, weights)
        sq_avg = decay * sq_avg + (1 - decay) * (grad ** 2)
        weights -= lr * grad / (np.sqrt(sq_avg) + eps)
    return weights, mse_loss(features, targets, weights)

def adam_optimizer(features, targets, start_weights=None, lr=0.01, steps=1000, b1=0.9, b2=0.999, eps=1e-8):
    weights = np.zeros(2) if start_weights is None else np.array(start_weights, dtype=float)
    m, v = np.zeros_like(weights), np.zeros_like(weights)
    for t in range(1, steps + 1):
        grad = calc_gradients(features, targets, weights)
        m = b1 * m + (1 - b1) * grad
        v = b2 * v + (1 - b2) * (grad ** 2)
        m_corr = m / (1 - b1**t)
        v_corr = v / (1 - b2**t)
        weights -= lr * m_corr / (np.sqrt(v_corr) + eps)
    return weights, mse_loss(features, targets, weights)
