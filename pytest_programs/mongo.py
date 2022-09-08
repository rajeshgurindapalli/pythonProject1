from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['Python']
info = db.Python
student1 = {"Reg No":"2100040361","Name": "Sumanth"}
student2 = [

    {"Reg No":"2100040365","Name": "Sasikanth"},
    {"Reg No":"2100040368","Name": "Yasash Chandra"},
    {"Reg No":"2100040354","Name": "Anish"},
    {"Reg No":"2100040356","Name": "Phani"},
]
#Creating Collections (Student Collection)
studentdata = db.student

#inserting Data
#studentdata.insert_one(student1)
#inserting many data
studentdata.insert_many(student2)

#fetching one data
#print(studentdata.find_one()

#fetching specific data
tofind1 = {"Reg No":"2100040368"}
for x in tofind1:
    print(studentdata.find_one(tofind1))

#delete one data
#todelete1 = {"Reg No":"2100040361"}
#studentdata.delete_one(todelete1)
#print(todelete1.delete_count,"documents deleted")

#Delete Many Data
todelete2 = {"Reg No":"2100040354"}
studentdata.delete_many(todelete2)