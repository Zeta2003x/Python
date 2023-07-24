import re

a = re.compile(r"\d{2}-\d{6}-\d{3}")
b = a.search("My phone number is 17-342234-234")
print("Phone number extracted:", b.group())