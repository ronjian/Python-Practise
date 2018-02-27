from time import sleep

class withClass:
    def __init__(self):
        print("initialize")
        
    def __enter__(self):
        print("entered")
        
    def __exit__(self, e_t, e_v, t_b):
        print("exited")

with withClass() as ins:
    for i in range(2):
        print("in the loop")
        sleep(1)

