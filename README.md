# Idea-Seminar
import rhinoscriptsyntax as rs
import math


class Turtle:

    def __init__(self, pos = [0,0,0], heading = [1,0,0]):

        self.heading = heading

        self.point = rs.AddPoint(pos)

        pointPos = rs.PointCoordinates(self.point)

        self.direction = rs.VectorCreate(heading,pointPos)

        self.lines = []



    def forward(self,magnitude):

        print (self.direction)

        movement = rs.VectorScale(self.direction,magnitude)

        prevPos = rs.PointCoordinates(self.point)

        rs.MoveObject(self.point,movement)

        currentPos = rs.PointCoordinates(self.point)

        rs.AddLine(prevPos,currentPos)



    def left(self,angle):

        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])

        print(self.direction)



    def right(self,angle):

        self.direction = rs.VectorRotate(self.direction, -angle, [0,0,1])

        print(self.direction)



    def goto(self, x, y):

        prevPos = rs.PointCoordinates(self.point)

        movement = rs.VectorCreate([x,y,0],prevPos)

        rs.MoveObject(self.point,movement)

        currentPos = rs.PointCoordinates(self.point)

        rs.AddLine(prevPos,currentPos)



    def jump(self, force, dis):
#make three points that together they can make an Arc, the first point would be heading position)
        distance=rs.VectorScale(self.direction,dis)
        startPoint= rs.PointCoordinates(self.point)
        endpoint= [startPoint[0] + distance.X , startPoint[1] + distance.Y, startPoint[2] + distance.Z]
        midpoint= [startPoint[0] + distance.X/2 , startPoint[1] + distance.Y/2, startPoint[2] + distance.Z/2]
        rotatevec= rs.VectorRotate(self.direction, 90, [0,0,1])
        heightvec=rs.VectorScale(rotatevec,force)
        midpoint1= rs.AddPoint(midpoint)
        forcepoint=rs.MoveObject(midpoint1,heightvec)
        jumppath2=rs.AddCurve([startPoint, forcepoint, endpoint])
        jumppath3=rs.AddInterpCurve([startPoint, forcepoint, endpoint])
        
rs.EnableRedraw(True)
        
t = Turtle()
for i in range (20):
    t.jump(i, i/2+10)
    t.forward(i/2+10)
    
    i=i+1
    #jump forward
