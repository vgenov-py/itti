import re

reg = '\w{1}:\s|\w{1}\.\s'

with open("questions.json") as file:
    data = file.read()

data = re.sub(reg, '', data)
print(data)

with open("questions_clean.json", "w") as file:
    file.write(data)
