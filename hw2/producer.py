#!/usr/bin/python3
import os
import random
import time
import sys


def random(min_value, max_value):
    return random.randint(min_value, max_value)

N = random(120, 180)

for i in range(N):
    x = random(1, 9)
    y = random(1, 9)
    o = random.choice(['+', '-', '*', '/'])

    exp = f"{x} {o} {y}"
    print(exp)
    sys.stdout.flush()

    time.sleep(1)

os._exit(os.EX_OK)