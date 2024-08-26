 # Class variable
class Employee:
        # class variable
        _minSaraly = 12000
        _maxSalary = 50000
        _companyName = 'บริษัท XYZ จำกัด'

        def __init__(self, name, salary, department):
        # instance variable
            self.__name = name
            self.__salary = salary
            self._department = department

    # private method
        def _showData(self):
            print('ชื่อพนักงาน = {}'.format(self.__name))
            print('เงินเดือน = {}'.format(self.__salary))
            print('ตำแหน่ง = {}'.format(self._department))
        


obj1 = Employee("Nopphadol",25000,'บัญชี')
print('เงินเดือนตำสุดของพนักงานคือ {}'.format(Employee._maxSalary))
print(Employee._companyName)

# 1:57:32
