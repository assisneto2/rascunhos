def reflex2D(self):
    for i in range(0, self.points.lenght):
        dom = Matrix(2, 1, [self.points[i][0],self.points[i][1]])
        z = Matrix(2, 2)

        z[1,1] = 1
        z[2,2] = -1

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
    return points

def refley2D(self):
    for i in range(0, self.points.lenght):
        dom = Matrix(2, 1, [self.points[i][0],self.points[i][1]])
        z = Matrix(2, 2)

        z[1,1] = -1
        z[2,2] = 1

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
    return points

def projx2D(self):
    for i in range(0, self.points.lenght):
        dom = Matrix(2, 1, [self.points[i][0],self.points[i][1]])
        z = Matrix(2, 2)

        z[1,1] = 1
        z[2,2] = 0

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
    return points

def projy2D(self):
    for i in range(0, self.points.lenght):
        dom = Matrix(2, 1, [self.points[i][0],self.points[i][1]])
        z = Matrix(2, 2)

        z[1,1] = 0
        z[2,2] = 1

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
    return points

def transla2D(self,x,y):
    for i in range(0, self.points.lenght):
        dom = Matrix(3, 1, [self.points[i][0],self.points[i][1], 1])
        z = Matrix(3, 3)

        z[1,1] = 1
        z[2,2] = 1
        z[1,3] = x
        z[2,3] = y
        z[3,3] = 1

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
    return points

def cisalhamento(self, ang):
    ang = ang * 180 / pi
    for i in range(0, self.points.lenght):
        dom = Matrix(2, 1, [self.points[i][0],self.points[i][1]])
        z = Matrix(2, 2)
        z[1,2] = tan(ang)
        z[1,1] = 1
        z[2,2] = 1

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
    return points
        
def rotate2D(self, ang):
    ang = ang * 180 / pi
    for i in range(0, self.points.lenght):
        dom = Matrix(2, 1, [self.points[i][0],self.points[i][1]])
        z = Matrix(2, 2)
        z[1,1] = cos(ang)
        z[1,2] = -sin(ang)
        z[2,1] = sin(ang)
        z[2,2] = cos(ang)

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
    return points

def reflex3D(self, point):
    x,y,z = point
    dom = matrix (3 , 1 , [x,y,z])
    k = Matrix(3,3)

    k[1,1] = 1 
    k[2,2] = -1
    k[3,3] = -1 

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1]
return [x,y,z]

def refley3D(self, point):
    x,y,z = point
    dom = matrix (3 , 1 , [x,y,z])
    k = Matrix(3,3)

    k[1,1] = -1 
    k[2,2] = 1
    k[3,3] = -1 

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1]
return [x,y,z]

def reflez3D(self, point):
    x,y,z = point
    dom = matrix (3 , 1 , [x,y,z])
    k = Matrix(3,3)

    k[1,1] = -1 
    k[2,2] = -1
    k[3,3] = 1 

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1]
return [x,y,z]


def projx3D(self, point):
    x,y,z = point
    dom = Matrix(3, 1, [x,y,z])
    k = Matrix(3,3)

    k[1,1] = 1
    k[2,2] = 0
    k[3,3] = 0

    dom = k.dot(dom)
    self.points[i][0] = dom[1,1]
    self.points[i][1] = dom[2,1]
    self.points[i][2] = dom[3,1]
return [x,y,z]

def projy3D(self, point):
    x,y,z = point
    dom = Matrix(3, 1, [x,y,z])
    k = Matrix(3,3)

    k[1,1] = 0
    k[2,2] = 1
    k[3,3] = 0

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1] 
return [x,y,z]

def projz3D(self, point):
    x,y,z = point
    dom = Matrix(3, 1, [x,y,z])
    k = Matrix(3,3)

    k[1,1] = 0
    k[2,2] = 0
    k[3,3] = 1

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1] 
return [x,y,z]

def rotatex3D(self, point,ang):
    x,y,z = point
    dom = Matrix(3, 1, [x,y,z])
    k = Matrix(3,3)

    k[1,1] = 1
    k[2,2] = cos(ang)
    k[2,3] = -sin(ang)
    k[2,3] = sin(ang)
    k[3,3] = cos(ang)

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1] 
return [x,y,z]

def rotatey3D(self, point,ang):
    x,y,z = point
    dom = Matrix(3, 1, [x,y,z])
    k = Matrix(3,3)

    k[1,1] = sin(ang)
    k[1,2] = cos(ang) 
    k[1,2] = -sin(ang) 
    k[2,2] = 1
    k[3,3] = cos(ang)

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1] 
return [x,y,z]


    def rotateY(self, ang): 
        ang = ang * pi / 180
        cos = math.cos(ang)
        sin = math.cos(ang) 
        z = (self.z * cos - self.x * sin)
        x = (self.z * sin + self.x *cos)
        return rotate3D(x , self.y , z)

    def rotateZ(self, ang): 
        ang = ang * pi / 180
        cos = math.cos(ang)
        sin = math.cos(ang) 
        x = (self.x * cos - self.y * sin)
        y = (self.x * sin + self.y *cos)
        return rotate3D(x , y , self.z)
