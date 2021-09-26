import math
import random

tol = 1e-50
max_iter = 100

class Expression:
    def __init__(self):
        pass

    def __add__(self, other): 
        if isinstance(other, (int, float)):
            other = Num(other)

        return Add(self, other)

    def __sub__(self, other): 
        if isinstance(other, (int, float)):
            other = Num(other)

        return Sub(self, other)

    def __mul__(self, other): 
        if isinstance(other, (int, float)):
            other = Num(other)

        return Mul(self, other)

    def __truediv__(self, other): 
        if isinstance(other, (int, float)):
            other = Num(other)

        return Div(self, other)

    def __pow__(self, other): 
        if isinstance(other, (int, float)):
            other = Num(other)

        return Pow(self, other)

    def exp(self): 
        return Exp(self)

    def log(self): 
        return Log(self)

class Num(Expression):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def subs(self, x):
        return self.num
        
    def diff(self):
        return Num(0.0)

    def __repr__(self):
        return f'{self.num}'

class Variable(Expression):
    def __init__(self):
        super().__init__()
    
    def subs(self, x):
        return x
    
    def diff(self):
        return Num(1.0)
        
    def __repr__(self):
        return 'x'

class Add(Expression):
    def __init__(self, expr1, expr2):
        super().__init__()
        self.expr1 = expr1
        self.expr2 = expr2
    
    def subs(self, x):
        return self.expr1.subs(x) + self.expr2.subs(x)
    
    def diff(self):
        return self.expr1.diff() + self.expr2.diff()

    def __repr__(self):
        return f'({self.expr1} + {self.expr2})'

class Sub(Expression):
    def __init__(self, expr1, expr2):
        super().__init__()
        self.expr1 = expr1
        self.expr2 = expr2
    
    def subs(self, x):
        return self.expr1.subs(x) - self.expr2.subs(x)
    
    def diff(self):
        return self.expr1.diff() - self.expr2.diff()

    def __repr__(self):
        return f'({self.expr1} - {self.expr2})'

class Mul(Expression):
    def __init__(self, expr1, expr2):
        super().__init__()
        self.expr1 = expr1
        self.expr2 = expr2
    
    def subs(self, x):
        return self.expr1.subs(x) * self.expr2.subs(x)
    
    def diff(self):
        t1 = self.expr1
        t2 = self.expr2
        t3 = self.expr1.diff()
        t4 = self.expr2.diff()

        return t2 * t3 + t1 * t4

    def __repr__(self):
        return f'({self.expr1} * {self.expr2})'

class Div(Expression):
    def __init__(self, expr1, expr2):
        super().__init__()
        self.expr1 = expr1
        self.expr2 = expr2
    
    def subs(self, x):
        return self.expr1.subs(x) / self.expr2.subs(x)
    
    def diff(self):
        t1 = self.expr1
        t2 = self.expr2
        t3 = self.expr1.diff()
        t4 = self.expr2.diff()

        return (t2 * t3 - t1 * t4)/(t2 * t2)

    def __repr__(self):
        return f'({self.expr1} / {self.expr2})'

class Pow(Expression):
    def __init__(self, expr1, expr2):
        super().__init__()
        self.expr1 = expr1
        self.expr2 = expr2
    
    def subs(self, x):
        return self.expr1.subs(x) ** self.expr2.subs(x)
    
    def diff(self):
        t1 = self.expr1
        t2 = self.expr2
        t3 = self.expr1.diff()
        t4 = self.expr2.diff()

        return (t1 ** (t2 - 1)) * (t2 * t3 + t1 * Log(t3) * t4)

    def __repr__(self):
        return f'({self.expr1} ** {self.expr2})'

class Exp(Expression):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr
    
    def subs(self, x):
        return math.exp(self.expr.subs(x))
    
    def diff(self):
        return self * self.expr.diff()

    def __repr__(self):
        return f'log({self.expr1})'

class Log(Expression):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr
    
    def subs(self, x):
        return math.log(self.expr.subs(x))

    def diff(self):
        return self.expr.diff() / self.expr

    def __repr__(self):
        return f'log({self.expr1})'


x = Variable()