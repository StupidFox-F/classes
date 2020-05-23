def once(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@once
def get_logger():
    return [1, 2, 3] * 2

print(get_logger)
print(get_logger())
print(id(get_logger), id(get_logger))


def get_logger_1():
    return [1, 2, 3] * 2
a1 = get_logger_1()
a2 = get_logger_1()

print(get_logger_1)
print(id(a1), id(a2))
print(a1 == a2)
print(a1)
