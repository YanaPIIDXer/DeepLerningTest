import numpy as np

def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    bias = -0.7
    if (np.sum(x * w) + bias) > 0: return 1
    return 0

print("=== AND ===")
print(and_gate(0, 0))
print(and_gate(0, 1))
print(and_gate(1, 0))
print(and_gate(1, 1))
