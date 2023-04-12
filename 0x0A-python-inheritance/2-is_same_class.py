
#!/usr/bin/python3
"""Checks if object is an instance of a class and returns true"""
def is_same_class(obj, a_class):
    """obj (any) is  The object to check whether is exactly an instance ."""
    if type(obj) == a_class:
                 return True
    return False
