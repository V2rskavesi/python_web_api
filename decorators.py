import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("in the decorator")
        func()
        print("after the decorator")
    return function_that_runs_func

@my_decorator
def my_function():
    print("i'm the function")

# my_function()

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("in the decorator")
            if number === 56:
                print("not running the function")
            else:
                func(*args, **kwargs)
            print("after the decorator")
        return function_that_runs_func
    return my_decorator




@decorator_with_arguments(56)
def my_function_too():
    print("hello")

my_function_too()
