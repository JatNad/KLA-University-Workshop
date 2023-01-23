interest=open('POI.txt','r')
file1=open('Source.txt','r')
file2=open('output.txt','w')

class polygon(object):
    def __init__(self):
        self.boundary='boundary\n'
        self.layer=file1.readline()
        self.datatype=file1.readline()
        self.coordinates=file1.readline()
        self.vertices=self.coordinates.split()
        self.edges=int(self.vertices[1])-1 #number of sides in polynomial
        self.edgelength=[]
        i=2
        while(i<len(self.vertices)-2):
            temp=(int(self.vertices[i])-int(self.vertices[i+2]))**2+(int(self.vertices[i+1])-int(self.vertices[i+3]))**2
            self.edgelength.append(temp) #stores length of each side of polynomial
            i+=2
        self.endel=file1.readline()
    def paste(self): #function to print object
        file2.write(self.boundary)
        file2.write(self.layer)
        file2.write(self.datatype)
        file2.write(self.coordinates)
        file2.write(self.endel)

class POI(object):
    def __init__(self):
        self.boundary='boundary\n'
        self.layer=interest.readline()
        self.datatype=interest.readline()
        self.coordinates=interest.readline()
        self.vertices=self.coordinates.split()
        self.edges=int(self.vertices[1])-1
        self.edgelength=[]
        i=2
        while(i<len(self.vertices)-2):
            temp=(int(self.vertices[i])-int(self.vertices[i+2]))**2+(int(self.vertices[i+1])-int(self.vertices[i+3]))**2
            self.edgelength.append(temp)
            i+=2
        self.endel=interest.readline()

def first(): #function to print the header
    while(True):
        x=file1.readline()
        if(x=='boundary\n'):
            return            
        else:
            file2.write(x)

def getpoi(): #function to extract poi information
    while(True):
        x=interest.readline()
        if(x=='boundary\n'):
            object=POI()
            return object

def check(poi,object): #function to compare poi and source object
    if(poi.edges==object.edges):
        temp=object.edgelength.index(max(object.edgelength)) #rotates the list containing the edge lengths such
        object.edgelength=object.edgelength[temp:]+object.edgelength[:temp] #that the longest edge is in the front
        if(poi.edgelength==object.edgelength):
            object.paste()

first()
poi=getpoi() 
interest.close()

while(True):
    object=polygon()
    check(poi,object)
    x=file1.readline()
    if(x!='boundary\n'):
        break

file2.write('endstr\n')
file2.write('endlib')

file1.close()
file2.close()
