import random


print("this line\n has some\n line breaks")

print("a\tb\tcat\tdogma")

print(10, 20, 30, 40, sep="\t")
print(100, 2000, 30000, 40000, sep="\t")

"""

i = 1
pi = 3.14159
print("normal string {i} {pi}")
print(f"formatted string {i} {pi}")
print(f"tau {pi + pi}")
"""
"""
import sys
print("logging", file=sys.stderr)

"""
"""
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

"""