class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    y = None
    if self.a <= x:
      if (self.a % 3 == 0 and self.a % 4 == 0):
          y = self.a
      self.a += 1
      if y is not None:
          return y
      else:
          return self.__next__()
        
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

x = int(input())
for y in myiter:
  print(y)


