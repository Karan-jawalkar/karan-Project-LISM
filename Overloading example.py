class A:

	def display(self, i=None):
		if i is None:
			print 'Null value'
		else:
			print 'value is'
		
obj = A()
obj.display()
