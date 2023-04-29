class Class:
    def __init__(self, string):
        self.string = string

    def getstring(self):
        self.string = input()
        
    def printstring(self):
        print(self.string.upper())


p = Class("")
p.getstring()
p.printstring()
