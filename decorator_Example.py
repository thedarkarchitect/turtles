import time 

def delay_decorator(func):
    def wrapper_funciton():
        time.sleep(2)
        #Do something before
        func()
        func()
        #do something after
    return wrapper_funciton

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

#decorated methods will delay none decorated methods wont delay
say_greeting()

say_hello()
say_bye()

