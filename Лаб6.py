def lowercase_args(func):
    """Декоратор: робить усі рядкові аргументи lowercase."""
    def wrapper(*args, **kwargs):
        new_args = [a.lower() if isinstance(a, str) else a for a in args]
        new_kwargs = {k: (v.lower() if isinstance(v, str) else v) for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper


@lowercase_args
def greet(name, message):
    print(f"{message}, {name}!")


if __name__ == "__main__":  # точка входу (можна видалити, якщо не треба)
    greet("ALICE", "HeLLo")
