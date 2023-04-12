#!/usr/bin/python3
"""
This code returns the list of all available attributes
and the methods of the object
"""


def lookup(obj):
  """
  This functions searches and returns a list of an object's available attributes.
  """
    return (dir(obj))
