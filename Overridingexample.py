#  Overriding example

class Parent:  				#parent class
	def display_method(self):
		print 'In Parent class'

class Child(Parent):  			#child class
	def display_method(self):
		print 'In child class'

c = Child()
c.display_method()

