import Rhino.Geometry as rg

pts = []

for i in range(10):
    for j in range(20):
        pts.append(rg.Point3d(i,j,30))

a = pts
