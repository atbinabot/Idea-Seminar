import rhinoscriptsyntax as rs
import math

theta = 10
angle = 0
i = 0
r = 100
steps = 200
offset = 50
points = []
while i < steps:
    angle += theta
    x = r * math.sin( angle * math.pi / 180)
    y = r * math.cos(angle * math.pi / 180)
    z = i * 2
    if i % 3 == 0:
        normal = rs.VectorCreate([x,y,z],[0,0,z])
        normal = rs.VectorScale(normal, 1/rs.VectorLength(normal))
        offsetVector = rs.VectorScale(normal,offset)
        p = rs.AddPoint(x,y,z)
#        rs.MoveObject(p,offsetVector)
    else:
        p = rs.AddPoint(x,y,z)
    points.append(p)
    i +=1
Curve=rs.AddCurve(points)
rs.DeleteObjects(points)

theta = 1
angle = 3
i = 0
r = 100
steps = 200
offset = 50
points = []
while i < steps:
    angle += theta
    x = r * math.sin( angle * math.pi / 180)
    y = r * math.cos(angle * math.pi / 180)
    z = i * 2
    if i % 3 == 0:
        normal = rs.VectorCreate([x,y,z],[0,0,z])
        normal = rs.VectorScale(normal, 1/rs.VectorLength(normal))
        offsetVector = rs.VectorScale(normal,offset)
        p = rs.AddPoint(x,y,z)
#        rs.MoveObject(p,offsetVector)
    else:
        p = rs.AddPoint(x,y,z)
    points.append(p)
    i +=1
Curve2=rs.AddCurve(points)
Curve2=rs.RotateObject(Curve2, (0,0,0), 180)
rs.DeleteObjects(points)


class CurveTangentPoint:
    def __init__ ( self , _c1 , _numberD , _scale ):
        self.c1= _c1
        self.numberD= _numberD
        self.scale= _scale
    def param (self):
        #print " check "
        dome = rs.CurveDomain(self.c1 )
        #print dome
        #domain remaping
        domemin = dome[0]
        domemax = dome[1]
        pointList1 = []
        pointList2= []
        #iterations of i
        for i in range (0 , self.numberD+1):
            #parameter defined to evaluate the tangent of curve
            parameter= (domemax-domemin)/self.numberD * i
            pt= rs.EvaluateCurve(self.c1 , parameter)
            tn= rs.CurveTangent(self.c1 , parameter)
            tn= rs.VectorUnitize(tn)
            tn= rs.VectorScale (tn , self.scale )
            point1= rs.AddPoint(pt)
            rs.AddPoint(tn)
            point2= rs.VectorAdd(pt , tn)
            rs.AddLine (pt , point2)
            pointList1.append(point1)
            pointList2.append (point2)
        return [pointList1 ,pointList2]
            
        
curve = Curve
curve2 = Curve2
num = int(100)
scaleVector= int(100)
obj1 = CurveTangentPoint(curve, num ,scaleVector  )
data1= obj1.param ()
obj2 = CurveTangentPoint(curve2, num ,scaleVector  )
data2= obj2.param ()
ptlistc11 = data1 [0]# point on curve
ptlistc12 = data1 [1]# tg points
ptlistc21= data2 [0]
ptlistc22= data2 [1]
count = 0
for i in ptlistc11:
    curvePt = [ ptlistc11[count] , ptlistc12 [count] , ptlistc21[ count], ptlistc22[count]]
    curveBetween2lists = rs.AddCurve(curvePt)
    count +=1
curveTg1 = rs.AddCurve ( ptlistc12)
curveTg2 = rs.AddCurve ( ptlistc22)

