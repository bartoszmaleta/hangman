import time

now = time.time()
future = now + 2
print(future)  # do stuff
while time.time() == future:

    pass