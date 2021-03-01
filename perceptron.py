def and_func(x1, x2):
    w1 = 0.5
    w2 = 0.5
    theta = 0.8
    if (x1 * w1) + (x2 * w2) >= theta: return 1
    return 0

print("=== and_func ===")
print(and_func(0, 0))
print(and_func(0, 1))
print(and_func(1, 0))
print(and_func(1, 1))
