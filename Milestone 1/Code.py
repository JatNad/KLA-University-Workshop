file1=open('Format_Source.txt','r')
file2=open('output.txt','w')

class polygon(object):
    def __init__(self):
        self.boundary='boundary\n'
        self.layer=file1.readline()
        self.datatype=file1.readline()
        self.coordinates=file1.readline()
        self.vertices=self.coordinates.split()
        self.edges=int(self.vertices[1])-1
        self.edgelength=[]
        i=2
        while(i<len(self.vertices)-2):
            temp=(int(self.vertices[i])-int(self.vertices[i+2]))**2+(int(self.vertices[i+1])-int(self.vertices[i+3]))**2
            self.edgelength.append(temp)
            i+=2
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
