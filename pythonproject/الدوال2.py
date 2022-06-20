def vote(age):
    def allow():
        print('allowed')
    def not_allowed():
        print('not allowed')
    if age>=18:
        return allow
    else:
        return not_allowed 
person1= vote(18)
person2=vote(15)
person1()
person2()

def decorator(function):
    def inner ():
        print("="*20)
        function()
        print("="*20)
    return inner
def write():
    print("Hello World")
write=decorator(write)
write()

