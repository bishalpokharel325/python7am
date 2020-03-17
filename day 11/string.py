message="we are learning pyuthon"
print(dir(message))
print(message.upper())
print(message.capitalize())
print(message.casefold())

username="hello admin"
x=username.replace("admin","ram")
"""replace garnu parema"""
print(x)

message="       Hello Python, we are learning python"
count=message.count("python")
print(count)
"""count python within string"""

"""print without unessary space"""
trimmed=message.lstrip()
print(trimmed)

x=message.replace(" ","")
print(x)
"""find gerne"""
print(message.find("we"))
print(message.center(200))
"""suru dekhi kati space lene"""
print(message.center(20))
print(message.capitalize())
"""first lai capitalize garne"""
print(message.encode())
print(message.index("are"))
"""text chai huna parxa"""
print(message.endwith("python"))
print(message.join("ram"))
message="hello, we are, learning"
sep=","
print(message.split())
"""into list"""
"""to undo this message"""
print(message.split(","))