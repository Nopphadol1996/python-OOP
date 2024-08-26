 # Encapsulation
class Employee:

    # def __init__(self, name, salary, department):
    #     # public attribute คนอื่นสามารถแก้ไขได้
    #     self.name = name
    #     self.salary = salary
    #     self.department = department

    # # public method
    # def showData(self):
    #     print('ชื่อพนักงาน = {}'.format(self.name))
    #     print('เงินเดือน = {}'.format(self.salary))
    #     print('ตำแหน่ง = {}'.format(self.department))

    #     def __init__(self, name, salary, department):
    #     # protected attribute เติม _ข้างหน้า
    #         self._name = name
    #         self._salary = salary
    #         self._department = department

    # # public method
    #     def _showData(self):
    #         print('ชื่อพนักงาน = {}'.format(self._name))
    #         print('เงินเดือน = {}'.format(self._salary))
    #         print('ตำแหน่ง = {}'.format(self._department))


        def __init__(self, name, salary, department):
        # private attribute เติม _ข้างหน้า
            self._name = name # protected
            self.__salary = salary
            self.__department = department
            self.__showData() # เมื่อตั้ง method เป็น private ไม่สามารถเรียกได้ ต้องเรียกภายใน class ของมันเอง

    # public method
        def __showData(self):
            print('ชื่อพนักงาน = {}'.format(self._name))
            print('เงินเดือน = {}'.format(self.__salary))
            print('ตำแหน่ง = {}'.format(self.__department))



# obj1 = Employee('Somchai', 50000, 'บัญขี')
# # public คนอื่นสามารถแก้ไขได้
# obj1.salary = 100000
# obj1.showData()

''' Protected'''
# obj1 = Employee('Somchai', 50000, 'บัญขี')
# # obj1.name = 'โจโจ้'
# # obj1._name = 'โจโจ้'
# # print(obj1._name)
# obj1.showData()

'''private'''

obj1 = Employee('Somchai', 50000, 'บัญขี')
obj1._name = 'Nopphadol'
obj1.__salary = 5000000
obj1.__department  = 'ฝ่ายขาย' # ไม่สามารถแก้ไขได้เพราะเป็น private
# obj1._showData()

