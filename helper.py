def calCircumference(radius:float)->float:
     return 2* (22/7) * radius

def calcAreaOFCircle(radius=None,diameter=None):
    pi=22/7
    if radius is not None:
        return pi*radius**2
    elif diameter is not None:
        return pi (diameter/2)*2