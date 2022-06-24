def even_parameters(function):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg % 2 != 0:
                return 'Please use only even numbers!'
        return function(*args)
    return wrapper


@even_parameters
def add(*args):
    return sum(args)
