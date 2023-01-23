interest=open('POI.txt','r')
file1=open('Source.txt','r')
file2=open('output.txt','w')

ans1=[]
ans2=[]

class polygon(object):
    def __init__(self,poi_edges):
        self.boundary='boundary\n'
        self.layer=file1.readline()
        self.datatype=file1.readline()
        self.coordinates=file1.readline()
        self.vertices=self.coordinates.split()
        self.edges=int(self.vertices[1])-1 #number of sides in polynomial
        self.edgelength=[]
        if(self.edges==poi_edges): #calculates length of edges only if source object has same number of edges as poi
            i=2
            while(i<len(self.vertices)-2):
                temp=(int(self.vertices[i])-int(self.vertices[i+2]))**2+(int(self.vertices[i+1])-int(self.vertices[i+3]))**2
                self.edgelength.append(temp) #stores length of each side of polynomial
                i+=2
        self.endel=file1.readline()
        self.topleft=[] #list stores the coordinates with lower x and y values
        self.topleft.append(int(self.vertices[2]))
        self.topleft.append(int(self.vertices[3]))
        i=4
        while(i<len(self.vertices)):
            self.topleft[0]=min(self.topleft[0],int(self.vertices[i]))
            self.topleft[1]=min(self.topleft[1],int(self.vertices[i+1]))
            i+=2
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
        self.topleft=[]
        self.topleft.append(int(self.vertices[2]))
        self.topleft.append(int(self.vertices[3]))
        i=4
        while(i<len(self.vertices)):
            self.topleft[0]=min(self.topleft[0],int(self.vertices[i]))
            self.topleft[1]=min(self.topleft[1],int(self.vertices[i+1]))
            i+=2

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

def check(poi,object,flag): #function to compare poi and source object
    if(poi.edges==object.edges):
        temp=object.edgelength.index(max(object.edgelength)) #rotates the list containing the edge lengths such
        object.edgelength=object.edgelength[temp:]+object.edgelength[:temp] #that the longest edge is in the front
        if(poi.edgelength==object.edgelength):
            if(flag==1): #source object matched with poi1
                ans1.append(object)
            else: #source object matched with poi2
                ans2.append(object)

def dist(obj1,obj2): #Function to return distance between 2 polygons
    return((obj1.topleft[0]-obj2.topleft[0])**2+(obj1.topleft[1]-obj2.topleft[1])**2)

first()
poi1=getpoi()
temp=poi1.edgelength.index(max(poi1.edgelength)) #rotates the list containing the edge lengths such
poi1.edgelength=poi1.edgelength[temp:]+poi1.edgelength[:temp] #that the longest edge is in the front
poi2=getpoi()
interest.close()
compare=dist(poi1,poi2)

while(True):
    object=polygon(poi1.edges)
    check(poi1,object,1)
    check(poi2,object,2)
    x=file1.readline()
    if(x!='boundary\n'):
        break

for i in range(len(ans1)):
    for j in range(len(ans2)):
        if(dist(ans1[i],ans2[j])==compare): #distance between source objects is the same as distance between poi 1 and poi 2
            ans1[i].paste()
            ans2[j].paste()
            del ans2[j]
            break

file2.write('endstr\n')
file2.write('endlib')

file1.close()
file2.close()
