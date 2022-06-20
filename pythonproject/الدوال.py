def odd_numbers():
    for number in range(0,100):
        if number %2==0 :
            continue
        print(number,sep=',')
odd_numbers()


print('next')


def odd_numbers(start,end):
    for number in range(start,end):
        if number %2==0 :
            continue
        print(number,sep=',')
odd_numbers(0,10)

print('next')


def increase(x):
    return x+1
def decrease (x):
    return x-1
def calculate (operation,x):
    return operation(x)
print(calculate(increase,5))
print(calculate(decrease,4))
