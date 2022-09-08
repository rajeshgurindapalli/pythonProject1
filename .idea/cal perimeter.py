class Perimeter:
    def calPerimeterofRect(self,len,bre):
        lenght = len
        bredth = bre
        print("perimeter of rectangle is", 2*(lenght+bredth))
        print("area of rectangle is", lenght * bredth)
    def calareaofcircle(self,radius):
        r = radius
        print("perimeter of circle is", 2 * 3.14 * r)
        print("area of circle is", 3.14 * r * r)
    def calperimetertriangle(self,s1,s2,s3):
        side1=s1
        side2=s2
        side3=s3
        print("perimeter of triangle is", side1+side2+side3)
        print("area of circle is", 1/2 * (side1+side2+side3))
obj = Perimeter()
obj.calPerimeterofRect(5,5)
obj.calareaofcircle(10)
obj.calperimetertriangle(15,15,15)