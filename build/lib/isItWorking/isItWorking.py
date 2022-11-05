class multiply():
    def __init__(self):
        self.a = 3
        self.n = 7

    def myfunc(self):
      return lambda self.a : self.a * self.n

    mytripler = myfunc(self.a)

    print(mytripler(self.n))