from values import Values


class Simple_Calc(Values):
    def __init__(self,a,b):
        super().__init__(a,b)

    def multiply(self):
        return self.value_a*self.value_b
    
    def substract(self):
        return self.value_a-self.value_b

    def add(self):
        return self.value_a*self.value_b
    
    def devide(self):
        try:
            return self.value_a//self.value_b
        except ZeroDivisionError:
            return "can't devide by zero"

    