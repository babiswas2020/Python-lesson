import json

class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a} and {self.b}"
   def __add__(self,other):
       if isinstance(other,A):
          return other.a+self.a

if __name__=="__main__":
   a=A(4,5)
   print(a)
   b=A(5,6)
   print(b)
   print(json.dumps(a.__dict__))
   print(json.dumps(b.__dict__))
   print(a+b)
   print(isinstance(a,A))
   print(isinstance(b,A))
   print(hasattr(a,'a'))
   print(hasattr(a,'b'))

