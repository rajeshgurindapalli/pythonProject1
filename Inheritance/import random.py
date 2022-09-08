import random
n=random.randbytes(3)

print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["jadeja","kohli","ben stokes","root"]
mylist1=["jadeja","kohli","ben stokes","root"]
print(random.choice(mylist))
random.shuffle(mylist)