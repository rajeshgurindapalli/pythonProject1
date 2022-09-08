from inhert.single import single1
from inhert.multilevel import multi
class e(single1,multi):
    def init(self):
        obj1=single2(50)
        obj2=multi(100)
        print(obj1.x+obj2.y)
obj=e()