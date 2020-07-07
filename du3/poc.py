import sys

toFactor = 3977
a = 3

def getS(p1, p2):
    try:
        if p1[0] == p2[0] and p1[1] == p2[1]:
            inv = pow(2*p1[1],-1,toFactor)
            return ((3*(p1[0]**2)+a)*inv) % toFactor
        else:
            inv = pow(p1[0]-p2[0],-1,toFactor)
            return ((p1[1]-p2[1])*inv) % toFactor
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print(e)
        print(p1,p2)
        print(p1[0]-p2[0])

def addPoints(p1, p2):
    if p1[0] == 0 and p1[1] == 0:
        return p2
    if p2[0] == 0 and p2[1] == 0:
        return p1
    s = getS(p1,p2)
    x3 = ((s**2)-p1[0]-p2[0]) % toFactor
    y3 = (-p1[1]+s*(p1[0]-x3)) % toFactor
    return [x3,y3]

e = 360360

p = [0,1]
q = [0,0]
while e > 0:
    if e % 2 == 1:
        q = addPoints(q,p)

    print(q)
    p = addPoints(p,p)
    e = e // 2
    print(p)

'''
res = p
for i in range(e):
    res = addPoints(res,p)
    print(res)
'''