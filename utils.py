from timeit import default_timer as timer

def timefunc(func):
    def inner(*args, **kwargs):
        start = timer()
        results = func(*args, **kwargs)
        end = timer()
        print(f"{func.__name__} took {end - start} seconds")
        return results
    return inner

def mac_addr(bytestring):
    return ':'.join("{:02x}".format(piece).upper() for piece in bytestring)