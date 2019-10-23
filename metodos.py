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



def reflex3D(self):
    for i in range(0 , self.points.lenght)
        dom = matrix (3 , 1 , [self.points[i][0] , self.points[i][1], 1])
        z = Matrix(3,3)

        z[1,1] = 1 
        z[2,2] = -1
        z[3,3] = 1 

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
        self.points[i][2] = dom[3,1]
    return points

def refley3D(self):
    for i in range(0 , self.points.lenght)
        dom = matrix (3 , 1 , [self.points[i][0] , self.points[i][1], 1])
        z = Matrix(3,3)

        z[1,1] = -1 
        z[2,2] = 1
        z[3,3] = 1 

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
        self.points[i][2] = dom[3,1]
    return points

def reflez3D(self):
    for i in range(0 , self.points.lenght)
        dom = matrix (3 , 1 , [self.points[i][0] , self.points[i][1], 1])
        z = Matrix(3,3)

        z[1,1] = 1 
        z[2,2] = 1
        z[3,3] = 1 

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
        self.points[i][2] = dom[3,1]
    return points


def projx3D(self):
    for i in range(0, self.points.lenght):
        dom = Matrix(3, 1, [self.points[i][0],self.points[i][1], 1])
        z = Matrix(3,3)

        z[1,1] = 1
        z[2,2] = 0
        z[3,3] = 0

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
        self.points[i][2] = dom[3,1]
    return points

def projy3D(self):
    for i in range(0, self.points.lenght):
        dom = Matrix(3, 1, [self.points[i][0],self.points[i][1], 1])
        z = Matrix(3,3)

        z[1,1] = 0
        z[2,2] = 1
        z[3,3] = 0

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
        self.points[i][2] = dom[3,1] 
    return points

def projz3D(self):
    for i in range(0, self.points.lenght):
        dom = Matrix(3, 1, [self.points[i][0],self.points[i][1], 1])
        z = Matrix(3,3)

        z[1,1] = 0
        z[2,2] = 0
        z[3,3] = 1

        dom = z.dot(dom)
        self.points[i][0] = dom[1,1]
        self.points[i][1] = dom[2,1]
        self.points[i][2] = dom[3,1] 
    return points

"""
import sys, math, pygame
from operator import itemgetter

rotação do eixo x 
""" 
class rotate3D: 
    def __init__(self , x = 0 , y = 0 , z = 0): 
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def rotateX(self, ang): 
        ang = ang * pi / 180
        cos = math.cos(ang)
        sin = math.cos(ang) 
        y = (self.y * cos - self.z * sin)
        z = (self.y * sin + self.z *cos)
        return rotate3D(self.x , y , z)

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
