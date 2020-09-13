import math

class cone:
    def __init__(self,radius,height):
        self.r = radius
        self.h = height

    def volume(self):
         #math.pi = 3.14
        volume = math.pi *(self.r**2)*self.h/3
        print("VOLUME = ",volume,"\n")

    def surface_area(self):
        length = math.sqrt((self.h**2)+(self.r**2))
        surfacearea_of_base = math.pi*(self.r**2)
        surfacearea_of_side = math.pi *self.r*length
        print("SURFACE AREA OF BASE = ",surfacearea_of_base,'\nSURFACE AREA OF SIDE = ',surfacearea_of_side,"\n")


cone1= cone(2,1)
cone1.surface_area()
cone1.volume()