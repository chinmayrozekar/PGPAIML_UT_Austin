# How to define a class in Python:

# The first Letter of the data type (Class) must be Capital.

class My_data_type:
    def init_some_vals(self, val2):     # self is first argument of func
        self.first_var = 1.7            # attribute named self.attribute name
        self.second_var = val2          # This func sets some attribute values
    def multiply_vals(self):
        return self.first_var * self.second_var
    
me = My_data_type()   # Declare an Object of the class My_data_type
me.init_some_vals(2.2)
print(me.first_var)
print(me.multiply_vals())




