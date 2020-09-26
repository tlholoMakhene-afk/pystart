#i have some behaviour that i want to implement -> i write some __function__  (these are called datamodel methods)
# there is a top level function/syntax -> that has coresponding __ function
    #if i want to add two objects(x+y) -> i use the __add__ function
    #if i want to initialise x -> i use __init__
    # repr(x) -> __repr__
    # x() -> __call__
class Polynomial:
    #class that represents polynomial
    #want to represent it as a class

    def __init__(self, *coeffs):
        self.coeffs = coeffs

    #this method will display the representation of our class or tyhe instance of that class as it's called
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self,other):
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))

    def __len__(self): 
        return len(self.coeffs)
    
    def __call__(self):
        pass
 
#p1 = Polynomial()
#p2 = Polynomial()
#p1.coeffs = 1,2,3 #x^2 + 2x + 3
#p2.coeffs = 3,4,3 #3^2 + 4x + 3

#instead of the above four lines,  we have the two lines below
p1 = Polynomial(1,2,3)
print('first Polynomial: ')
print(p1)
p2 = Polynomial(3,4,3)
print('second Polynomial: ')
print(p2)
#adding Polynomial
print('adding two Polynomials and creating a new Polynomial with both the other Polynomial added together')
print(p1+p2)







