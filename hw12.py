from math import log2

def get_cross_entropy(p, q):
    """
    Calculates the cross-entropy between distribution p and q.
    Formula: H(p, q) = sum(p[i] * log2(1/q[i]))
    """
    entropy_val = 0
    for i in range(len(p)):
        # Added a small epsilon to prevent log(0) errors
        safe_q = max(q[i], 1e-10)
        entropy_val += p[i] * log2(1 / safe_q)
    return entropy_val

def find_optimal_distribution(p, initial_q, max_steps, step_size):
    """
    Uses a Hill Climbing approach to adjust q until it minimizes cross-entropy.
    The moves are designed to keep the sum of q equal to 1.
    """
    q = list(initial_q)
    n = len(q)
    
    for i in range(1, max_steps + 1):
        current_loss = get_cross_entropy(p, q)
        best_neighbor = None
        min_loss = current_loss

        # Generate possible moves (neighbors)
        # We increase one index by 'h' and decrease others proportionally to keep sum=1
        for target_idx in range(n):
            for direction in [1, -1]: # Try both increasing and decreasing
                neighbor = list(q)
                h = step_size * direction
                
                # Adjust the target element
                neighbor[target_idx] += h
                
                # Distribute the change among other elements to maintain sum of 1
                adjustment = h / (n - 1)
                for other_idx in range(n):
                    if other_idx != target_idx:
                        neighbor[other_idx] -= adjustment
                
                # Check if this move is valid (no negative probabilities)
                if any(val < 0 for val in neighbor):
                    continue
                    
                new_loss = get_cross_entropy(p, neighbor)
                if new_loss < min_loss:
                    min_loss = new_loss
                    best_neighbor = neighbor

        # If we found a better distribution, move there; otherwise, stop
        if best_neighbor:
            q = best_neighbor
            if i % 10 == 0:
                print(f"Iteration {i}: Loss = {min_loss:.5f}, q = {q}")
        else:
            break
            
    return q

if __name__ == '__main__':
    # Target distribution (p)
    target_p = [0.5, 0.25, 0.25]
    
    # Initial guess (q) - must sum to 1
    initial_guess = [0.333, 0.333, 0.334]
    
    limit = 500
    step = 0.001
    
    final_q = find_optimal_distribution(target_p, initial_guess, limit, step)
    
    print("-" * 30)
    print(f"Target p: {target_p}")
    print(f"Final  q: {[round(x, 4) for x in final_q]}")
    print(f"Minimum Cross-Entropy achieved: {get_cross_entropy(target_p, final_q):.5f}")
    print(f"Entropy H(p): {get_cross_entropy(target_p, target_p):.5f}")
