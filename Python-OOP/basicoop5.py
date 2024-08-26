 # ฟังก์ชั่นเสริม
class Employee:

    def __init__(self, name, salary, department): # constrctor
        self.name = name # self.name is Attribute --> name is parametor
        self.salary = salary
        self.department = department

    # สร้าง method
    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('ตำแหน่ง = {}'.format(self.department))


#การสร้างวัตถุ instance
obj1 = Employee('Somchai', 50000, 'บัญขี')
obj2 = Employee('Somsri', 60000, 'โปรแกรมเมอร์')
obj3 = Employee('Somsak', 70000, 'ผู้จัดการ')

# Check ว่า obj1 ถูกสร้างมาจาก class Employee ไหม
# print(isinstance(obj1,Employee))

# print(dir(obj1))

# print(obj1.__class__)
