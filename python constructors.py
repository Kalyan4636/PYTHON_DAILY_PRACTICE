#python constructors

class ComplexNumber:
    def __init__(self,r=0,i=1):
        self.real=r;
        self.imag=1;

    def getData(self):
        print('{0}+{1}j'.format(self.real,self.imag))

c1=ComplexNumber(5,6)
c1.getData()
