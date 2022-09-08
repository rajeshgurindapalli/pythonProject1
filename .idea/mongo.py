from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['PFSD']
info = db.PFSD
student1 = {"Reg Num":"2100030973","Name": "RAJESH"}
student2 = [
    {"Reg Num":"2100030632","Name":"MAHESH"},
    {"Reg Num":"2100030962","Name":"SAGAR"},
    {"Reg Num":"2100031050","Name":"BABAMAHESH"},
    {"Reg Num":"2100030678","Name":"KIRAN"}]
studentdata = db.student
studentdata.insert_one(student1)
studentdata.insert_many(student2)
tofind1 = {"Reg Num":"2100031050"}
for x in tofind1:
    print(studentdata.find_one(tofind1))
    todelete2 = {"Reg Num":"2100030632"}
    studentdata.delete_many(todelete2)