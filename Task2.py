import random
import string

def GP(L):
    C = string.ascii_letters + string.digits + string.punctuation
    P = ''.join(random.choice(C) for _ in range(L))
    return P

def main():
    while True:
        try:
            L = int(input("Enter the desired length of the password: "))
            if L < 1:
                raise ValueError("Password length should be at least 1.")
            break
        except ValueError as e:
            print(e)
    P = GP(L)
    print(f"Generated Password: {P}")
main()