import random
import sys

float = if "-fl" in sys.argv

try:
    problems = input("How many problems do you want: ")
    problems = int(problems)
except ValueError:
    print("[Error]: enter a number stupid!")
    sys.exit(0)

try:
    for i in range(1, int(problems)):
        if float:
            l = random.uniform(10.2, 500.20)
            r = random.uniform(1.1, 9.9)
        else:
            l = random.randint(1,500)
            r = random.randint(1,10)

        # shadow pad
        pad = "-"*pad

        q = l/r
        print(f"\nProblem {i}: {l}Ã·{r}?")
        while True:
            a = input(">")

            if float and a == f"{str(q):.2f}"::
                break
            if not float and int(a) == int(q):
                break

except KeyboardInterrupt:
    print("\nThanks for trying!")
    sys.exit(0)
