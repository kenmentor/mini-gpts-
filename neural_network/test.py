class Value:
  def __init__(self,data,_children=[], _op="" ,label=""):
    self._children = set(_children)
    self.data = data
    self._op = _op
    self.label = label
    self.grad = 0


  def __repr__(self):
      return f"data={self.data}.value {self.label}"

  def __add__ (self,other):
      return Value(other.data+self.data,(self,other) ,"+")
  def __mul__ (self,other):
    print(self._op)
    return Value(other.data*self.data ,(self,other), "*")
  # def __mul__ (self,other):
  #   return Value(other.data*self.data)
  # def __mul__ (self,other):
  #   return Value(other.data*self.data)
h = 0.001
a = Value(2)
b = Value(2)
c = a+b
e = Value(2+h)
d = e +c

f = Value(2)
L = f+d
k = Value((1/h))
# print((L+h).vale)





def stage ():
  h = 0.001
  a = Value(2.0)
  a.data+= h
  b = Value(-3.0)
  c = Value(10.0)
  e = a+b
  d = e +c
  d.label ="d"
  

  f = Value(-2)
  L = f+d
  L2 =L.data+h


  # print(L2.data - L.data)
#   print(L)
  print((L2-L.data)/h)
stage()

  