# صنف العقدة
class Node:
	# دالة لتهيئة كائن العقدة
	def __init__(self, data):
		self.data = data # إسناد البيانات
		self.next = None # null تهيئة العقدة اللاحقة لتكون

# صنف القائمة المترابطة الذي يحتوي على كائن عقدة
class LinkedList:

	# تهيئة رأس القائمة
	def __init__(self):
		self.head = None

	# دالة لإدراج عقدة في بداية القائمة
	def push(self, new_data):
		# 1: حجزم موقع العقدة في الذاكرة
		# 2: إضافة البيانات
		new_node = Node(new_data)

		# 3. جعل العقدة اللاحقة للعقدة الجديدة كرأس للقائمة
		new_node.next = self.head

		# 4: تحريك رأس القائمة ليشير إلى العقدة الجديدة.
		self.head = new_node

		# تطبع هذه الدالة محتويات القائمة المترابطة

	# يدرج هذا التابع عقدة جديدة بعد عقدة معطاة
	def insertAfter(self, prev_node, new_data):

		# 1: التحقق من أنّ العقدة المعطاة موجودة في القائمة المترابطة فعلاً
		if prev_node is None:
			print("The given previous node must inLinkedList.")
			return

		# 2: إنشاء عقدة جديدة
		# 3: إضافة البيانات
		new_node = Node(new_data)

		# 4: جعل العقدة التي تلي العقدة الجديدة هي العقدة التي تلي العقدة المعطاة
		new_node.next = prev_node.next

		# 5: جعل العقدة الجديدة هي العقدة التي تلي العقدة المعطاة
		prev_node.next = new_node

	# يُلحق التابع عقدة جديدة في نهاية القائمة المترابطة
	def append(self, new_data):

		# 1: إنشاء عقدة جديدة
		# 2: إضافة البيانات
		# 3: None جعل ما يلي العقدة هو
		new_node = Node(new_data)

		# 4: نجعل العقدة الجديدة رأسًا للقائمة
		# إن كانت القائمة المترابطة فارغة
		if self.head is None:
			self.head = new_node
			return

		# 5: وإلا فننتقل عبر عناصر القائمة وصولًا إلى العقدة الأخيرة
		last = self.head
		while (last.next):
			last = last.next

		# 6: نغير ما يلي العقدة الأخيرة
		last.next = new_node

	# تحذف الدالة أول ظهور للمفتاح المعطى في القائمة المترابطة
	# وذلك باستخدام إشارة إلى رأس القائمة والمفتاح المعطى
	def deleteNode(self, key):

		# تخزين عقدة الرأس
		temp = self.head

		# إن كانت عقدة الرأس تحمل قيمة المفتاح المعطى
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		# البحث عن المفتاح المراد حذفه مع متابعة
		# العقدة السابقة لأنّنا نحتاجها لتغير العقدة اللاحقة للعقدة السابقة
		# 'prev.next'
		while (temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# إن كان المفتاح غير موجود في القائمة المترابطة
		if (temp == None):
			return

		# فك ارتباط العقدة بالقائمة المترابطة
		prev.next = temp.next

		temp = None

	# بدءًا من العقدة المعطاة
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next

if __name__=='__main__':

	# نبدأ بقائمة مترابطة فارغة
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	''' 
	حجزت ثلاث كتل في الذاكرة ديناميكيًا
	ولدينا مؤشرات لهذه الكتل هي
	first, second, third

	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | None |	 | 2 | None |	 | 3 | None | 
	+----+------+	 +----+------+	 +----+------+ 
	'''

	llist.head.next = second # ربط العقدة الأولى بالثانية

	''' 
	تشير العقدة الأولى الآن إلى العقدة الثانية، وبهذا تكونان مترابطتين

	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | o-------->| 2 | null |	 | 3 | null | 
	+----+------+	 +----+------+	 +----+------+ 
	'''

	second.next = third # ربط العقدة الثانية بالثالثة

	''' 
	تشير العقدة الثانية إلى العقدة الثالثة، وبهذا تكونان مترابطتين


	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | o-------->| 2 | o-------->| 3 | null | 
	+----+------+	 +----+------+	 +----+------+ 
	'''


llist.push(7)

llist.insertAfter(llist.head,8)

llist.append(10)

llist.deleteNode(2)

llist.printList()