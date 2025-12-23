import timeit, math

def generate_trial_division_wheel(primes, wheel_size):
    residues = [
        i for i in range(1, wheel_size + 1) 
        if all(i % p != 0 for p in primes)
    ]

    # Compute gaps (distances between the residues)
    gaps = [residues[i+1] - residues[i] for i in range(len(residues) - 1)]
    gaps.append((wheel_size + residues[0]) - residues[-1])
    
    func_name = f"trial_division_wheel_{wheel_size}"
    code_lines = [f"def {func_name}(n):"]
    for p in primes:
        code_lines.append(f"    if n % {p} == 0: return {p}")
    
    code_lines.append(f"    sqrt_n = math.isqrt(n)")
    # Start with residues[1] which is next prime (skip 1)
    code_lines.append(f"    f = {residues[1]}")  
    code_lines.append(f"    while f <= sqrt_n:")
    
    # Rotate gaps because we started with residues[1]
    rotated_gaps = gaps[1:] + [gaps[0]] # 
    for gap in (rotated_gaps):  
        code_lines.append(f"        if n % f == 0: return f")
        code_lines.append(f"        f += {gap}")
    code_lines.append(f"    return n")
    
    namespace = {"math": math}
    exec("\n".join(code_lines), namespace)
    return namespace[func_name]

trial_division_wheel_6 = generate_trial_division_wheel([2,3], 6)
trial_division_wheel_30 = generate_trial_division_wheel([2,3,5], 30)
trial_division_wheel_210 = generate_trial_division_wheel([2,3,5,7], 210)
trial_division_wheel_2310 = generate_trial_division_wheel([2,3,5,7,11], 2310)
trial_division_wheel_30030 = generate_trial_division_wheel([2,3,5,7,11,13], 30030)
