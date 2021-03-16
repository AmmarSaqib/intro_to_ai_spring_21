# Lab 1 -  Intro. AI Dr. Aasia Khanum



### Task 1 (A):
Using a Python list create a Class named "*Stack*". The class should contain the push and pop methods. The item to be stored in the stack should be of the the class "*Node*" for which the class is given below:

```
class Node:

    def __init__ (self, _id, _value):
        self._id = _id
        self._value = _value
    
    def get_id(self):
        return self._id

    def get_value(self):
        return self._value
    
    def set_id(self, _id):
        self._id = _id

    def set_value(self, _value):
        self._value = _value
```