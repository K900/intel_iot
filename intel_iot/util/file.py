def write_file(filename, value):
    with open(filename, "w") as f:
        f.write(value)


def write_ignore_busy(filename, value):
    try:
        write_file(filename, value)
    except IOError as e:
        if e.errno == 16:
            pass
        else:
            raise e


def read_file(filename):
    with open(filename) as f:
        return f.read()
