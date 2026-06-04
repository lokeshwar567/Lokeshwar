def m_dec(fun):
    def wrapper(*args,**kwargs):
        print('before')
        result=fun(*args,**kwargs)
        print('after')
        return result
    return wrapper
def add(a,b):
    return a+b
add=m_dec(add)
print(add(3,4))