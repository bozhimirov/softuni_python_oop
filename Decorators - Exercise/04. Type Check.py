def type_check(type):
    def decorator(func):
        def wrapper(argument):
            if not isinstance(argument, type):
                return 'Bad Type'
            return func(argument)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
