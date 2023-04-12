
#!/usr/bin/python3

class BaseGeometry:
     """Reprsent base geometry."""
      """then the method is not implemented yet"""
       """then the Validation of the parameter as an integer."""

     def area(self):

           raise Exception("area() is not implemented")

     def integer_validator(self, name, value):

            if type(value) != int:

                   raise TypeError("{} must be an integer".format(name))     
             
             if value <= 0:
            
                 raise ValueError("{} must be greater than 0".format(name))

