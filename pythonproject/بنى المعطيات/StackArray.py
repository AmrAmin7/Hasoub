from sys import maxsize

# دالة لإنشاء المكدس وتهيئته ليكون بحجم 0
def createStack():
    stack = []
    return stack

# يكون المكدس فارغًا عندما يكون حجمه صفرًا
def isEmpty(stack):
    return len(stack) == 0

# دالة لإضافة عنصر إلى المكدس، وزيادة حجم المكدس بمقدار 1
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")

# دالة لحذف عنصر من المكدس، وإنقاص حجم المكدس بمقدار 1
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)  # تعيد القيمة سالب ما لا نهاية

    return stack.pop()


# اختبار الدوال السابقة
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")