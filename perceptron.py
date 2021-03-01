import numpy as np

def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    bias = -0.7
    if (np.sum(x * w) + bias) > 0: return 1
    return 0

def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    bias = -0.2
    if (np.sum(x * w) + bias) > 0: return 1
    return 0

def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    bias = 0.7
    if (np.sum(x * w) + bias) > 0: return 1
    return 0

def xor_gate(x1, x2):
    # 第１層
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    # 第２層
    return and_gate(s1 ,s2)

print("=== AND ===")
print(and_gate(0, 0))
print(and_gate(0, 1))
print(and_gate(1, 0))
print(and_gate(1, 1))

print("=== OR ===")
print(or_gate(0, 0))
print(or_gate(0, 1))
print(or_gate(1, 0))
print(or_gate(1, 1))

print("=== NAND ===")
print(nand_gate(0, 0))
print(nand_gate(0, 1))
print(nand_gate(1, 0))
print(nand_gate(1, 1))

print("=== XOR ===")
print(xor_gate(0, 0))
print(xor_gate(0, 1))
print(xor_gate(1, 0))
print(xor_gate(1, 1))
