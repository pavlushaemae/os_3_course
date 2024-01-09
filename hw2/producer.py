#!/usr/bin/python3
import os
import random
import time
import sys

N = random.radint(120, 180)

for i in range(N):
    x = random.radint(1, 9)
    y = random.radint(1, 9)
    o = random.choice(['+', '-', '*', '/'])

    exp = f"{x} {o} {y}"
    print(exp)
    sys.stdout.flush()

    time.sleep(1)

os._exit(os.EX_OK)
