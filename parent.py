#!/usr/bin/python3
import os
import sys
import random

n = int(sys.argv[1])

child_count = n

def fork():
    child_process_id = os.fork()
    if child_process_id > 0:
        pid = os.getpid()
        print(f'Parent[{pid}]: I ran children process with PID {child_process_id}.')
    else:
        random_number = random.randint(5, 10)
        os.execl('./child.py', './child.py', str(random_number))
    return child_process_id

while(child_count > 0):
    child_process_id = fork()
    if child_process_id > 0:
        child_count = child_count - 1

child_count = n
while(child_count > 0):
    child_process_id, child_status = os.wait()
    pid = os.getpid()
    print(f'Parent[{pid}]: Child with PID {child_process_id} terminated. Exit Status {child_status}.')
    if child_status:
        child_count = child_count - 1
    else:
        fork()
sys.exit(1)
