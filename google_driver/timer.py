import time

def timer(x: int, y: int):
    timing = time.time()
    second = 0
    while True:
        if time.time() - timing > x:
            timing = time.time()
            second += x
            print(f"{second} seconds")
            if second == y:
                print('Time end')
                break


