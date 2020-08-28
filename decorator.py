Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #nested function 구현하기
>>> def name_decorator(name):
    def decorator(func):
        def function(*args, **kargs):
            return func() + name
        return function
    return decorator

@name_decorator('정우성')
def greeting():
    return "Hello, "

print(greeting())
SyntaxError: invalid syntax
>>> 
>>> 