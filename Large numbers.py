import random;
import sys;

def fTask(bit):
    print("First Task.\n")
    print("Number of key variants:\n")
    variants = {}
    for i in bit:
        variants[i] = 2**i
        print(f"    for {i} bit:", 2**i, "variants. \n")
    return variants


def sTask(bit, vars):
    print("Second Task. \n")
    print("One hexadecimal takes 4 bits.")
    keys = []
    for i in bit:
        key = random.uniform(0, vars[i] - 1)
        keys.append(key) 
    print(keys)
    
64
def main():
    bit = [2**i for i in range (3,13)]
    # vars = fTask(bit)
    # sTask(bit, vars)
    # print(vars)
    # print(123.1123:.0f)
    print(sys.maxsize)

main()
