def gcd(a,b):
    '''
    Objective: To find the greatest common divisior
    Input parameter:
            a,b: Two number whose GCD need to find
    Return Value: GCD of two numbers
                
    '''
    if b == 0:
        return a
    else: return gcd(b,a%b)
class Rational:
       
    def __init__(self,numerator,denominator):
        '''
        Objective: To Construct the class
        Input parameter:
                Self: Object of the class
                Numerator of a rational number
                Denominator of a rational number
        Return Value: Rational number
                
        '''
        if denominator == 0:
            raise ZeroDivisionError("Denominator of zero should not be zero")
        else:
            g = gcd(numerator,denominator)
            self.numerator = numerator/g
            self.denominator = denominator/g
            
#Addition of rational number
    def __add__(self,other):
        '''
        Objective: To Add two rational number
        Input parameter:
                Self: Object of the class
                Other: Another object of the class
                Numerator of a rational number
                Denominator of a rational number
        Return Value: Addition of Rational number
                
        '''
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,self.denominator * other.denominator)
#Subtraction of rational number
    def __sub__(self,other):
        '''
        Objective: To Subtract two rational number
        Input parameter:
                Self: Object of the class
                Other: Another object of the class
                Numerator of a rational number
                Denominator of a rational number
        Return Value: Subtraction of Rational number
                
        '''
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,self.denominator * other.denominator)
#Multiplication of rational
    def __mul__(self,other):
        '''
        Objective: To Multiply two rational number
        Input parameter:
                Self: Object of the class
                Other: Another object of the class
                Numerator of a rational number
                Denominator of a rational number
        Return Value: Multiplication of  Rational number
                
        '''
        return Rational(self.numerator * other.numerator , other.denominator * self.denominator)
#division of rational number
    def __div__(self,other):
        '''
        Objective: To Divide two rational number
        Input parameter:
                Self: Object of the class
                Other: Another object of the class
                Numerator of a rational number
                Denominator of a rational number
        Return Value: Division of Rational number
                
        '''
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
    
