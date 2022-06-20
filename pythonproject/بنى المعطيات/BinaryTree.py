class newNode():

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


# التنقل عبر مستويات الشجرة الثنائية

def inorder(temp):
    if (not temp):
        return

    inorder(temp.left)
    print(temp.key, end=" ")
    inorder(temp.right)


# دالة لإدراج عنصر في الشجرة الثنائية

def insert(temp, key):
    q = []
    q.append(temp)

    # التنقل عبر مستويات الشجرة الثنائية بحثاً عن مكان فارغ
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)

        # اختبار الدوال السابقة


if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)

