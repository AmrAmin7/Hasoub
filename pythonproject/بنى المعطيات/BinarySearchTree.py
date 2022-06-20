# صنف مساعد يستخدم لتمثيل عقدة مفردة في شجرة البحث الثنائية
class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# دالة مساعدة لإدراج عقدة جديدة مع المفتاح المعطى
def insert(root,node):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

# دالة مساعدة لإجراء عملية التنقل الوسطي
def inorder(root):
	if root:
		inorder(root.left) #نطبع العقدة التى على يسار الجزر
		print(root.val)    #نطبع الجزر
		inorder(root.right) #نطبع العقدة التى على يمين الجزر


def search(root, key):
	# الحالة الأساسية: أن يكون الجذر فارغًا أو يكون المفتاح موجودًا في الجذر
	if root is None or root.val == key:
		return root

	# أن يكون المفتاح أكبر من مفتاح الجذر
	if root.val < key:
		return search(root.right, key)

	# أن يكون المفتاح أصغر من مفتاح الجذر
	return search(root.left, key)


def minValueNode(node):
	current = node

	# استخدام الحلقة التكرارية لإيجاد أبعد ورقة إلى جهة اليسار
	while (current.left is not None):
		current = current.left

	return current


# لدينا شجرة بحث ثنائية ومفتاح،
# وستحذف هذه الدالة المفتاح وتعيد الجذر الجديد

def deleteNode(root, key):
	# الحالة الأساسية
	if root is None:
		return root

	# إن كان المفتاح المراد حذفه أصغر من مفتح الجذر
	# فإن هذا يعني أنّ المفتاح يقع في الفرع الأيسر
	if key < root.val:
		root.left = deleteNode(root.left, key)

	# إن كان المفتاح المراد حذفه أكبر من مفتاح الجذر
	# فإن هذا يعني أنّ المفتاح يقع في الفرع الأيمن
	elif (key > root.val):
		root.right = deleteNode(root.right, key)

	# إن كان المفتاح مماثلًأ لمفتاح الجذر، فهذا يعني أنّ هذه العقدة
	# هي العقدة التي يجب حذفها
	else:

		# عقدة تمتلك ابنًا واحدًا أو لا تمتلك أبناء
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# عقدة تمتلك عقدتي أبناء. نحصل على العقدة اللاحقة الوسطية
		# أصغر عقدة في الفرع الأيمن
		temp = minValueNode(root.right)

		# نسخ محتويات العقدة اللاحقة الوسطية إلى هذه العقدة
		root.val = temp.val

		# حذف العقدة اللاحقة الوسطية
		root.right = deleteNode(root.right, temp.val)

	return root

# اختبار الدوال السابقة
# لننشئ شجرة البحث الثنائية التالية
#	 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

# طباعة نتيجة التنقل الوسطي
inorder(r)

x=search(r,20)
if x is None:
		print("the number not found")
else: print("the number {} is found ".format(x.val))

print("\nDelete 20")
root=deleteNode(r,20)

print("new tree")
inorder(r)
