def get_foobar_output(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FooBar"
    elif n % 3 == 0:
        return "Foo"
    elif n % 5 == 0:
        return "Bar"
    else:
        return str(n)


def print_foobar(start=1, end=101):
    for i in range(start, end):
        print(get_foobar_output(i))


if __name__ == "__main__":
    print_foobar()
