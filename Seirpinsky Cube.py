import rhinoscriptsyntax as rs
from random import *

B = [1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1]
strInput = rs.GetObject()
#print strInput


arrP = rs.BoundingBox(strInput)
strBox = rs.AddBox(arrP)


counter = 0

x0 = arrP[0][0]
y0 = arrP[0][1]
z0 = arrP[0][2]
x6 = arrP[6][0]
y6 = arrP[6][1]
z6 = arrP[6][2]
counter = 0
p = [[0 for i in range(0,3)] for j in range(0,27)]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            p[counter][0] = x0 + i / 3 * (x6 - x0)
            p[counter][1] = y0 + j / 3 * (y6 - y0)
            p[counter][2] = z0 + k / 3 * (z6 - z0)
            counter = counter + 1
for i in range(0,27):
    if (B[i] == 1):
        strV = rs.VectorCreate(p[i], p[0])
        strC = rs.CopyObject(strInput, strV)
        strS = rs.ScaleObject(strC, p[i], [1/3,1/3,1/3])


#another method 

#for i in range(0,27):
#    rs.AddPoint(p[i])

#p0 = [x0,y0 + 0 * (y6 - y0) ,z0]
#p1 = [x0,y0 + 0.333333 * (y6-y0), z0]
#p2 = [x0,y0 + 0.666666 * (y6-y0), z0]
#p3 = [x0 + 0.333333 * (x6-x0), y0, z0]
#p4 = [x0 + 0.333333 * (x6-x0), y0 + 0.333333 * (y6-y0), z0]

rs.DeleteObject(strBox)

rs.DeleteObject(strInput)
