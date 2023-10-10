file = open("a.txt")
file.close()
# print(file.read())
# input(": ")
# print("Posición cursor: ",file.tell())
# input(": ")
# print(file.seek(0))
# input(": ")
# print("Posición cursor: ",file.tell())
# input(": ")
# print(file.read())
# input(": ")
# print("Posición cursor: ",file.tell())
# input(": ")
# print(file.read())

'''
Apertura y cierre #1:
'''
# file = open("a.txt")

# print(file.read())
# print(file.closed)
# file.close()
# print(file.closed)
'''
Apertura y cierre #2:
'''
# with open("a.txt") as file: # {
#     # enter
#     data = file.readlines()

#     # exit
# # };
# print(data)
# # print(data[0])

# b = "- ¿Qué tal?\n- Todo bien, tú?\n- Chau"
# b = b.split("\n")
# print(b)

'''
Escritura
'''
import datetime as dt

file = open("err.log", "a")

file.write(f"\n{dt.datetime.now()}|204|error cuando se eliminan valores")

file.close()