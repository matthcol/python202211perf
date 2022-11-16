import functools

def twice(func):
    @functools.wraps(func)
    def twice_wrapper():
        func()
        func()
    return twice_wrapper


@twice
def say_weather_forecast():
    """print weather forecast of today"""
    print("It's a sunny day")


def learn_python_decorator():
    """tutorial on python decorator"""
    print("Read the very good turorial here:")
    print("https://realpython.com/primer-on-python-decorators")

learn_python_decorator = twice(learn_python_decorator)

say_weather_forecast()

learn_python_decorator()