def valid(func):
    def inner(*args):
        for i in args:
            if i<0:
                print('error')
                return
        func(*a)
    return inner