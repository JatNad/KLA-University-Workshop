file1=open('Format_Source.txt','r')
file2=open('output.txt','w')

class polygon(object):
    def __init__(self,layer,datatype,coordinates,endel):
        self.boundary='boundary\n'
        self.layer=layer
        self.datatype=datatype
        self.coordinates=coordinates
        self.endel=endel
    def paste(self):
        file2.write(self.boundary)
        file2.write(self.layer)
        file2.write(self.datatype)
        file2.write(self.coordinates)
        file2.write(self.endel)

def first():
    while(True):
        x=file1.readline()
        if(x=='boundary\n'):
            return            
        else:
            file2.write(x)

count=2

first()
while(True):
    a=file1.readline()
    b=file1.readline()
    c=file1.readline()
    d=file1.readline()
    object=polygon(a,b,c,d)
    if(count>0):
        count-=1
        object.paste()
    x=file1.readline()
    if(x!='boundary\n'):
        break

file2.write('endstr\n')
file2.write('endlib')

file1.close()
file2.close()