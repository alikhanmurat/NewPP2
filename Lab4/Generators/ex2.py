class evennumbers:
    def __iter__(self):
        self.a = 2
        return self
        
    def __next__(self):
        while self.a <= x:
            y = self.a
            self.a += 2
            return y
        raise StopIteration

myclass = evennumbers()
myiter = iter(myclass)

x = int(input())
result = []
for y in myiter:
    result.append(str(y))
print(', '.join(result))
