import itertools
import random

def nd_riemann_sum(f, domain, grid_size):
    dims = len(domain)
    
    def compute_integral(axis_idx, current_pt):
        if axis_idx == dims:
            return f(*current_pt)
            
        start, end = domain[axis_idx]
        delta = (end - start) / grid_size[axis_idx]
        subtotal = 0.0
        
        for j in range(grid_size[axis_idx]):
            mid_val = start + (j + 0.5) * delta
            subtotal += compute_integral(axis_idx + 1, current_pt + [mid_val])
            
        return subtotal * delta
        
    return compute_integral(0, [])

def nd_monte_carlo(f, domain, num_points):
    dim_count = len(domain)
    running_sum = 0.0
    total_area = 1.0
    
    for low, high in domain:
        total_area *= (high - low)
        
    for _ in range(num_points):
        coords = [random.uniform(l, h) for l, h in domain]
        running_sum += f(*coords)
        
    return (running_sum / num_points) * total_area

def objective_fn(x, y, z):
    return x + y + z  

integration_range = [(0, 1), (0, 1), (0, 1)]
grid_resolution = [10, 10, 10]
n_samples = 100000

res_riemann = nd_riemann_sum(objective_fn, integration_range, grid_resolution)
res_monte = nd_monte_carlo(objective_fn, integration_range, n_samples)

print(f"Riemann Result: {res_riemann}")
print(f"Monte Carlo Result: {res_monte}")
