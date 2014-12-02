class Employee:
	empcount = 0
	def __init__(self, name, salary):
	      self.name = name
	      self.salary = salary
	      Employee.empcount +=1 #Employee.empcount + 1
   
        def displayCount(self):
     	      print "Total Employee %d" % Employee.empCount

   	def displayEmployee(self):
      	      print "Name : ", self.name,  ", Salary: ", self.salary

emp1 = Employee("karan", 200000)
emp2 = Employee("Shree", 300000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empcount
