def tags(string):
    def decorator(func):
        def wrapper(*args):
            return f'<{string}>{func(*args)}</{string}>'
        return wrapper
    return decorator

