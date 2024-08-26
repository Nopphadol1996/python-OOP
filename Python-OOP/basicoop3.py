class Employee: # การสร้าง class
    

    # สร้าง method
    def detial(self, name, salary, department):
        self.name = name # self.name is Attribute --> name is parametor
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('ตำแหน่ง = {}'.format(self.department))

#การสร้างวัตถุ instance
obj1 = Employee()
obj1.detial('Somchai', 50000, 'บัญขี')
print('--------------------------------------')

obj2 = Employee()
obj2.detial('Somsri', 60000, 'โปรแกรมเมอร์')
print('--------------------------------------')

obj3 = Employee()
obj3.detial('Somsak', 70000, 'ผู้จัดการ')

obj1.showData()
# obj2.showData()
# obj3.showData()