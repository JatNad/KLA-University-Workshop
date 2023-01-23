file1=open('Format_Source.txt','r')
file2=open('output.txt','w')

class polygon(object):
    def __init__(self):
        self.boundary='boundary\n'
        self.layer=file1.readline()
        self.datatype=file1.readline()
        self.coordinates=file1.readline()
        self.endel=file1.readline()
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
    object=polygon()
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
