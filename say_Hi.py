import time


def greeting(func):
    def wrapper_func():
        name = input("May I know your name please? ")
        rec_name = func(name)
        print(f"Hi there, {rec_name}")
        time.sleep(5)
        print("Would you fancy to grab a drink?...")
    wrapper_func()

# name = input("May I know your name? ")
@greeting
def hi(name):
    return name