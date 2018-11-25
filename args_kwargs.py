def my_method(arg1, arg2):
    return arg1 + arg2

my_method(5, 6)

def my_log_method(arg1, arg2, arg3, arg4):
    return arg1 + arg2 + arg3 + arg4

def my_list_adddition(list_args):
    return sum(list_arg)

my_long_method(3,5,7,12)

my_list_adddition([3,5,7,12,15,234,23])

def addition_simplified(*args):
    return sum(args)

addition_simplified(3,4,5,34,3,43,34,43,34)


##
# *args is a catchall term for arguments
# meaning that its a list(tuple?) of all arguments passed in

# **kwargs is the same but for key-value arguments
def what_are_kwargs(name, location):
    print(name)
    print(location)

what_are_kwargs(name='Jose', location='UK')
