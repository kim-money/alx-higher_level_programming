#!/usr/bin/python3
"""Defines an inherited class-checking function."""
def inherits_from(obj, a_class):
    """  If obj is an inherited instance of a_class - True.
        Otherwise - False."""


     return (issubclass(type(obj), a_class) and type(obj) != a_class)

