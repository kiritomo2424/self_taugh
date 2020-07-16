import re

line = "The ghost thas says boo haunts the loo baoo"
m = re.findall(".oo",line,re.IGNORECASE)


print(m)
