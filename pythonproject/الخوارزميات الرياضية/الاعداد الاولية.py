def isPrime(n):
    # إن كان العدد المعطى أقل من 1 أو يساويه تعيد الدالة قيمة خاطئة
    if (n <= 1):
        return False

    # n - 1 التحقق ضمن النطاق 2 و
    for i in range(2, n):
        if (n % i == 0):
            return False

    return True


# اختبار الدالة السابقة
if isPrime(11):
    print("true")
else:
    print("false")

    
