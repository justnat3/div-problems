import random
import sys

float = "-fl" in sys.argv

try:
    problems = input("How many problems do you want: ")
    problems = int(problems)
except ValueError:
    print("[Error]: enter a number stupid!")
    sys.exit(0)

try:
    for i in range(0, int(problems)):
        if float:
            l = random.uniform(10.2, 500.20)
            r = random.uniform(1.1, 9.9)
        else:
            l = random.randint(1,500)
            r = random.randint(1,10)

        q = l/r
        print(f"\nProblem {i+1}: {l:.2f}Ã·{r:.2f}?")
        while True:
            a = input(">")

            try:
                if float and round(a, 2) == round(q, 2):
                    break
                if not float and int(a) == int(q):
                    break

            except ValueError:
                continue

except KeyboardInterrupt:
    print("\nThanks for trying!")
    sys.exit(0)
