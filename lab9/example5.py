import time

def simple_timer(t):
    if t==0:
        print("ENDED!!")
        return 0
    else:
        print("remaining time:",t)
        time.sleep(1)
        return simple_timer(t-1)

print(simple_timer(6))