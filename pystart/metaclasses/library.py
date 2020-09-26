class Base:
    def foo(self):
        return 'foo'

#scenario you create library code, how do you make sure that the user code creator(the business unit code creator) doesnt break your code

class BaseClass:
    def food(self):
        return self.bald()

#we cant use the assert hasattr on library code

#we could use try catch but we'd only see the error at runtime

    #try:
        
    #except expression as identifier:
      #pass 

#python is much simpler than C# or java 
#it is a protocol orientated language
 