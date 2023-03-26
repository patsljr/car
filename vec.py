import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def unit_vector(self):
        magnitude = math.sqrt(self.x**2 + self.y**2)
        u = Vector(self.x/magnitude, self.y/magnitude)
        return u
    
    def nominal(self, margin):
        if (abs(self.x - self.y) < margin):
            return True
        else:
            return False
    def angle(self):
        if (self.y > 0 and self.x > 0):
            return math.atan(abs(self.y/self.x))
        elif(self.y > 0 and self.x == 0):
            return 90
        elif(self.y > 0 and self.x < 0):
            return 90 - math.atan(abs(self.y/self.x))
        elif(self.y == 0 and self.x < 0):
            return 180
        elif(self.y < 0 and self.x < 0):
            return 180 + math.atan(abs(self.y/self.x))
        elif(self.y < 0 and self.x == 0):
            return 270
        elif(self.y < 0 and self.x > 0):
            return 360 - math.atan(abs(self.y/self.x))
        else:
            return 360
    
class wheel_vec():
    def __init__(self, left, right):
        self.l = left
        self.r = right
       
def substract(vec1, vec2):
    return Vector(vec1.x - vec2.x, vec1.y - vec2.y)

def pdiv(vec1, vec2):
    return Vector(vec1.x/vec2.x, vec1.y/vec2.y)