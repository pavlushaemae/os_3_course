import os
import sys
import signal


def sigusr1(signum, frame):
    print(f"Produced: {produced}")
    sys.stdout.flush()

pipe1_0 = os.pipe()
pipe0_2 = os.pipe()
pipe2_0 = os.pipe()

signal.signal(signal.SIGUSR1, sigusr1)
produced = 0

p1 = os.fork()

if p1 == 0:
    os.close(pipe1_0[0])
    os.dup2(pipe1_0[1], sys.stdout.fileno())
    os.execve('./producer.py', ["producer"], {})
    os._exit(1)

p2 = os.fork()

if p2 == 0:
    os.close(pipe0_2[1])
    os.dup2(pipe0_2[0], sys.stdin.fileno())
    os.close(pipe2_0[0])
    os.dup2(pipe2_0[1], sys.stdout.fileno())
    os.execve("/usr/bin/bc", ["bc"], {})

    os._exit(1)

os.close(pipe1_0[1])
os.close(pipe0_2[0])
os.close(pipe2_0[1])

while True:
    exp = os.read(pipe1_0[0], 1024).decode("utf-8")
    if not exp:
        break

    os.write(pipe0_2[1], exp.encode("utf-8"))

    result = os.read(pipe2_0[0], 1024).decode("utf-8")
    print(f"{exp.strip()} = {result.strip()}")
    produced += 1

os.kill(p1, signal.SIGTERM)
os.kill(p2, signal.SIGTERM)