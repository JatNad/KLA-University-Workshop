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
        self.edges=int(self.vertices[1])-1
        self.edgelength=[]
        if(self.edges==poi_edges):
            i=2
            while(i<len(self.vertices)-2):
                temp=(int(self.vertices[i])-int(self.vertices[i+2]))**2+(int(self.vertices[i+1])-int(self.vertices[i+3]))**2
                self.edgelength.append(temp)
                i+=2
        self.endel=file1.readline()
        self.topleft=[]
        self.topleft.append(int(self.vertices[2]))
        self.topleft.append(int(self.vertices[3]))
        i=4
        while(i<len(self.vertices)):
            self.topleft[0]=min(self.topleft[0],int(self.vertices[i]))
            self.topleft[1]=min(self.topleft[1],int(self.vertices[i+1]))
            i+=2
    def paste(self):
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

def first():
    while(True):
        x=file1.readline()
        if(x=='boundary\n'):
            return            
        else:
            file2.write(x)

def getpoi():
    while(True):
        x=interest.readline()
        if(x=='boundary\n'):
            object=POI()
            return object

def check(poi,object,flag):
    if(poi.edges==object.edges):
        temp=object.edgelength.index(max(object.edgelength))
        object.edgelength=object.edgelength[temp:]+object.edgelength[:temp]
        if(flag==1):
            if(poi.edgelength==object.edgelength and object.layer=='layer 1\n'):            
                ans1.append(object)
        else:
            if(poi.edgelength==object.edgelength and object.layer=='layer 2\n'):
                ans2.append(object)

def dist(obj1,obj2):
    return((obj1.topleft[0]-obj2.topleft[0])**2+(obj1.topleft[1]-obj2.topleft[1])**2)

first()
poi1=getpoi()
temp=poi1.edgelength.index(max(poi1.edgelength))
poi1.edgelength=poi1.edgelength[temp:]+poi1.edgelength[:temp]
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
        if(dist(ans1[i],ans2[j])==compare):
            ans1[i].paste()
            ans2[j].paste()
            del ans2[j]
            break

file2.write('endstr\n')
file2.write('endlib')

file1.close()
file2.close()