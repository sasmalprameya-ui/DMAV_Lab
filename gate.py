def step(x):
    return 1 if x>0 else 0

def and_gate(x1,x2):
    return step(-12 + 8*x1 + 8*x2)

def or_gate(x1,x2):
    return step(-4 +8*x1 + 8*x2)

def main():
    print("Available gates: and , or")
    gate= input("Enter the gate name:").strip().lower()

    print ("\nTruth Table\n")
    print("x1 x2 |output")
    print("--------------")

    for x1 in [0,1]:
        for x2 in [0,1]:
            if gate == "and":
                result = and_gate(x1,x2)
            elif gate == "or":
                result = or_gate(x1,x2)

            print(f"{x1} {x2} | {result}")


