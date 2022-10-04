import random
import time
import decimal

# На жаль не зміг реалізувати генерацію ключів більш ніж на 1024 біти. Буду радий почути якісь поради

def fTask(bit): #Перше завдання
    print("\nFirst Task.\n")
    print("Number of key variants:")
    variants = {}
    for i in bit:
        variants[i] = 2**i
        print(f"    for {i} bit:", 2**i, "variants.")
    return variants


def sTask(bit, vars): #Друге завдання
    print("\nSecond Task. \n")
    keys = []
    print("Generated keys:")
    for i in bit:
        key = hex(int(float(str(decimal.Decimal(random.random()) * (vars[i] - 1)))))
        keys.append(key) 
    print(keys)
    return keys
    
def tTask(bit,keys): #Третє завдання
    print("\nThird Task.\n")
    print("Key brute force time")
    passwords = []
    hex = "0123456789abcdef"
    for i in range(len(keys)):
        print(f"    For {bit[i]} bit password:")
        password = ""
        start = time.time()
        for k in range(len(keys[i])-2):
            for letter in hex:         
                if letter == keys[i][k+2]:
                    time.sleep(0.00000000000001)
                    password += keys[i][k+2]
                    continue
        end = time.time() - start
        passwords.append("0x"+password)
        print(str(end)+" sec")
    print(f"\nPasswords: {passwords}")

def main(): 
    bit = [2**i for i in range (3,11)] 
    vars = fTask(bit)
    keys = sTask(bit, vars)
    tTask(bit, keys)

main()
