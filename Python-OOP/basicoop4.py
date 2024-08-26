 # การสร้าง constrctor
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

    # def __del__(self):
    #     # คืนค่าให้กับหน่วยความจำ
    #     print('Call destructor')

#การสร้างวัตถุ instance
obj1 = Employee('Somchai', 50000, 'บัญขี')
# สามารถแก้ไขค่าที่อยู่ใน attribut ได้ เพราะยังไม่ห่อหุ้มข้อมูล
obj1.name = 'Nopphadol'
obj1.salary = 70000

obj1.showData()
print('--------------------------------------')

obj2 = Employee('Somsri', 60000, 'โปรแกรมเมอร์')
obj2.showData()
print('--------------------------------------')

obj3 = Employee('Somsak', 70000, 'ผู้จัดการ')
obj3.showData()
