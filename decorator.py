def type_checker(function):
    def inner_func(digit1, digit2):
        if (type(digit1) !=int) or (type(digit2) != int):
            print("only integer support")
            return
        return function(digit1, digit2)
    return inner_func
            
@type_checker
def f(digit1, digit2):
    return digit1 * digit2


print(f(3, 1))