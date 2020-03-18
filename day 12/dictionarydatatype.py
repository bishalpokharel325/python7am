"""very important for JSON
integer data type nalene always string
"""
users={
    "name":"admin",
    "address":"kathmandu",
    "contact":{
        "phone": "01454544",
        "mobile":"98788858"
    }
}
"""print these data"""
print(users["name"])
print(users["contact"]['mobile'])
"""some inbuilt fuunctions"""
# print(dir(users))
"""
some dictionary methods:
1) get
2) keys
"""
print(users.keys())
print(users.get("contact"))
# users.pop("contact")
# print(users.keys())
print(users.values())
