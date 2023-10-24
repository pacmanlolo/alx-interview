#!/usr/bin/python3
"""This code determines if a given data
   set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """method that determines if data
       represents a valid UTF-8 encoding
       Args:
          data(List of intergers): data to verify
       Return:
          True or False
    """
    for i in range(len(data)):
        if data[i] > 255:
            return False
    return True
