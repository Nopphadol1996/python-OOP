# ชื่อ, เงินเดือน

class Employee: # การสร้าง class
    

    # สร้าง method
    def detial(self):
        self.name = 'ก้องรักสยาม'
        self.salary = 50000
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน {} ='.format(self.salary))

#การสร้างวัตถุ instance
emp1 = Employee()
emp1.detial()

