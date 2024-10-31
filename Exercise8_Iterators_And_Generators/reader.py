def read_next(*args):
    for arg in args:
        iterator = iter(arg)
        while True:
            try:
                yield next(iterator)
            except StopIteration:
                break
