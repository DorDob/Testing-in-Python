class Calculator:

    def add(self,a,b):
        return a + b

    def substract(self, a,b):
        return a - b

    def multiply (self, a,b):
        return a * b

    def divide(self, a, b):
        if b== 0:
            return False
        return a/b   #






if __name__ == "__main__":   # ten blok kodu nie wykona się w testach
    calc=Calculator()
    print(calc.add(1,2))