# قائمة مترابطة لتخزين الرتل
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# إنشاء صنف يمثل الرتل

# يخزن العنصر الأول في الرتل العقدة الأولى
# ويخزن العنصر الأخير العقدة الأخيرة في القائمة المترابطة
class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # يضيف التابع عنصرًا إلى الرتل


    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # يحذف التابع عنصرًا من الرتل


    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None
        return str(temp.data)


# اختبار التوابع السابقة
if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)

    print("Dequeued item is " + q.DeQueue())