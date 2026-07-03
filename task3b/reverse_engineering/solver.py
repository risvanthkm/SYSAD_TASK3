from z3 import *

alp_matrix = "CDIKNOSUW"

def base9(number, matrix):
    base9_digits=""
    decoded=""
    while number:
        remainder = number % 9
        base9_digits += str(remainder)
        number = number // 9
    base9_digits = base9_digits[::-1]
    for e in base9_digits:
        e = int(e)
        decoded += matrix[e]
    return decoded

b0 = BitVec('b0', 32)
b1 = BitVec('b1', 32)
b2 = BitVec('b2', 32)

solver = Solver()

solver.add((b0 + 1337) == 2007)
solver.add((b0 ^ b1) == 1570)
solver.add((b2 % b1) == 870)
solver.add((b2 / 2) == 22251)

if solver.check() == sat:
    model = solver.model()
    print(
        base9(model[b0].as_long(), alp_matrix), 
        base9(model[b1].as_long(), alp_matrix), 
        base9(model[b2].as_long(), alp_matrix), 
        sep="-"
    )
else:
    print("Unsatisfiable")

