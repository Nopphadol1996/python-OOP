 # Getter Setter Method
class Employee:
        
        def __init__(self, name, salary, department):
        # private attribute เติม __ข้างหน้า
            self.__name = name
            self.__salary = salary
            self.__department = department

    # private method
        def _showData(self):
            print('ชื่อพนักงาน = {}'.format(self.getName()))
            print('เงินเดือน = {}'.format(self.getSalary()))
            print('ตำแหน่ง = {}'.format(self.getDepartment()))
        
        # setter method = ปรับปรุงแก้ไขค่าใน attribute
        def setName(self, newname):
             self.__name = newname

        def setSalary(self, newsalary):
             self.__salary = newsalary

        def setDepartment(self, department):
             self.__department = department

        
        # Getter method
        def getName(self):
             return self.__name
        
        def getSalary(self):
             return self.__salary
        
        def getDepartment(self):
             return self.__department

'''private'''
# setter method
# obj1 = Employee('Somchai', 1, 'บัญขี')
# obj1.setName('Nopphadol')
# obj1.setSalary(5000000)
# obj1.setDepartment('ฝ่ายขาย')
# obj1._showData()


# getter method

obj1 = Employee("Nopphadol",25000,'บัญชี')
obj1._showData()
print('------------------------------')
obj2 = Employee('Somcahi',1500,'PSDV')

print(obj2.getName())
print(obj2.getSalary())
obj2.setSalary(25000)
print(obj2.getSalary())
# obj2._showData()

