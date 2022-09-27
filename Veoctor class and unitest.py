#!/usr/bin/env python
# coding: utf-8

# In[43]:


# Testing Python programs (networkx)

print("Tests for the Vector class using the 'unittest' module.")

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):      #  string "Vector(x, y, z)"
        return f"Vector({self.x!r},{self.y!r}, {self.z!r})"  

    def __eq__(self, other):   # v == w
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    
    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):   # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):   # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):  # multiplication - return the dot product (number or vector probably?)
        if isinstance (other, Vector): #to calculate vector result
            return self.x * other.x + self.y * other.y + self.z * other.z
        else: #to calculate number result
            return Vector(self.x * other, self.y * other, self.z * other)
        
    __rmul__ = __mul__

    def cross(self, other):   # return the cross product (Vector)
        return Vector(self.y * other.z - self.z * other.y, 
                      self.z * other.x - self.x * other.z, 
                      self.x * other.y - self.y * other.x)
        
    def length(self):   # the length of the vector
        return math.sqrt(self * self) 

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))

# Test 

import math 
import unittest

class TestVector(unittest.TestCase):
    
    def setUp(self):
        self.a = Vector(1, 1, 1)
        self.b = Vector(-1, -1, -1)
        
    def test_vector(self):
        self.assertEqual(self.a, self.a)
        self.assertNotEqual(self.a, self.b)
        self.assertEqual(self.a + self.b, Vector(0, 0, 0))
        self.assertEqual(self.a - self.b, Vector(2, 2, 2))
        self.assertEqual(self.a * self.b, -3)
        self.assertEqual(self.a * 2, Vector(2, 2, 2))
        self.assertEqual(3 * self.a, Vector(3, 3, 3))
        self.assertEqual(self.a.cross(self.b), Vector(0, 0, 0))
        
    def test_vector_hash(self):
        S = set([self.a, self.a, self.b])
        self.assertEqual(len(S), 2)
        self.assertTrue(self.a in S)
        self.assertTrue(self.b in S)
        
    def tearDown(self): pass
    
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 

#that (...) is because I work on interactive environment and simple() caused error


# In[ ]:




