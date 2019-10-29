class Transf:
    def reflex2D(self, point):
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = 1
        z[2,2] = -1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]
    
    def refley2D(self, point):
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = -1
        z[2,2] = 1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]

    def projx2D(self, point):
        x, y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = 1
        z[2,2] = 0

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]
    
    def projy2D(self, point):
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        
        z[1,1] = 0
        z[2,2] = 1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]
    
    def transla2D(self, point,x,y):
        xp, yp = point
        dom = Matrix(3, 1, [xp,yp, 1])
        z = Matrix(3, 3)
        
        z[1,1] = 1
        z[2,2] = 1
        z[1,3] = x
        z[2,3] = y
        z[3,3] = 1

        dom = z.dot(dom)
        xp = dom[1,1]
        yp = dom[2,1]
        return [xp,yp]

    def cisalhamento(self,point, ang):
        ang = ang * pi / 180
        x,y = point
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        z[1,2] = tan(ang)
        z[1,1] = 1
        z[2,2] = 1

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]

    def rotate2D(self, point, ang):
        x,y = point
        ang = ang * pi / 180
        dom = Matrix(2, 1, [x,y])
        z = Matrix(2, 2)
        z[1,1] = cos(ang)
        z[1,2] = -sin(ang)
        z[2,1] = sin(ang)
        z[2,2] = cos(ang)

        dom = z.dot(dom)
        x = dom[1,1]
        y = dom[2,1]
        return [x,y]

    def escalonamento(self, point, x, y):
        xp,yp = point
        dom = Matrix(2, 1, [xp,yp])
        z = Matrix(2, 2)
        z[1,1] = x
        z[2,2] = y

        dom = z.dot(dom)
        xp = dom[1,1]
        yp = dom[2,1]
        return [xp,yp]

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
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1]
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

    k[1,1] = cos(ang)
    k[1,2] = -sin(ang) 
    k[2,1] = sin(ang) 
    k[2,2] = 1
    k[3,3] = cos(ang)

    dom = k.dot(dom)
    x = dom[1,1]
    y = dom[2,1]
    z = dom[3,1] 
return [x,y,z]


def rotatez3D(self, point,ang):
    x,y,z = point
    dom = Matrix(3, 1, [x,y,z])
    k = Matrix(3,3)

    k[1,1] = cos(ang)
    k[1,2] = -sin(ang) 
    k[2,1] = sin(ang) 
    k[2,2] = cos(ang)
    k[3,3] = 1

    dom = k.dot(dom)
    x = dom[1,1] #
    y = dom[2,1] #
    z = dom[3,1] #
return [x,y,z]

