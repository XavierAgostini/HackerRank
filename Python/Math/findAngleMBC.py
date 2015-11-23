import math

AB = float(raw_input())
BC = float(raw_input())
M = math.sqrt(AB**2 + BC**2)*0.5
angle = int(round(math.degrees(math.atan(AB/BC))))
print "%s°" % angle
