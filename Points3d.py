from math import sqrt
class point3d:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
    def distance(self,point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2)
point1 = point3d(6,2,5)
point2 = point3d(7,0,3)
point3 = point3d(4,2,9)
print(point1)
print(point2)
print(point3)    
print(point1.distance(point2))
print(point2.distance(point3))
print(point3.distance(point1))

    
    
    