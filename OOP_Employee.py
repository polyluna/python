class Employee:
        
        raise_amount = 1.04
        num_of_emps=0

        def __init__(self,first,last,pay):
                self.first = first
                self.last = last
                self.pay = pay
                self.email = first + '.' + last + '@company.com'
                Employee.num_of_emps +=1

        def fullname(self):
                return '{} {}'.format(self.first, self.last)
        
                self.pay=int(self.pay * self.raise_amount)

class Developer (Employee):
        def __init__(self,first,last,pay,prog_lang):
                super().__init__(first, last, pay)
                self.prog_lang = prog_lang

class Manager (Employee):
        def __init__(self,first,last,pay,employees = None):
                super().__init__(first, last, pay)
                if employees is None:
                        self.employees = []
                else:
                        self.employees = employees

        def add_emp(self, emp):
                if emp not in self.employees:
                        self.employees.append(emp)
        def remove_emp(self, emp):
                if emp in self.employees:
                        self.employees.remove(emp)
        def print_emps(self):
                for emp in self.employees:
                        print('-->', emp.fullname())



dev_2 = Developer('Test', 'User', 60000,'Java')
man_1 = Manager('Corey', 'Schafer', 50000,[dev_2])



# dev_1.apply_raise()

# print(man_1.email)
man_1.print_emps()

print(issubclass (Developer, Employee))