import math
class gameObject:
    def __init__(self, pos, radius):
        self.pos=pos
        self.radius=radius
def distance(Coord_1,Coord_2):
    if len(Coord_1) != len(Coord_2)
        return "The length of the vectors is not equal"
    else:
        l=[(Coord_1[i]-Coord_2[i])**2 for i in range(len(Coord_1))]
        return math.sqrt(sum(l))
def collisions(x,y):
    Coord_x = x.pos
    Coord_y = y.pos
    impact = x.radius + y.radius
    if distance(Coord_x, Coord_y) <= impact:
    return "boom"
