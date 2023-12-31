m_course = [{
	"name": "Patricia",
	"id" :  "001",
  "score": 9
},
{
	"name": "Nicole",
	"id" :  "002",
  "score": 6.6
},
{
	"name": "Javier",
	"id" :  "003",
  "score": 10
},
{
	"name": "Verónica",
	"id" :  "004",
  "score": 8.6
},
{
	"name": "Guillermo",
	"id" :  "005",
  "score": 4
},
{
	"name": "Pablo",
	"id" :  "006",
  "score": 9
}
]

a_course =[
{
	"name": "Germán",
	"id" :  "001",
  "score": 6.8
},
{
	"name": "Sara",
	"id" :  "002",
  "score": 8.8
},
{
	"name": "Jorge",
	"id" :  "003",
  "score": 3.3
},
{
	"name": "María",
	"id" :  "004",
  "score": 9.8
},
{
	"name": "Alicia",
	"id" :  "005",
  "score": 5.6
},
{
	"name": "Hernesto",
	"id" :  "006",
  "score": 6.8
}]

courses = m_course
courses.extend(a_course)

def get_score(name:str) -> float:
    '''Función que permite encontrar nota por nombre de estudiante en un determinado curso.'''
    name = name.lower()
    for student in courses:
        if student.get("name").lower() == name:
            return student.get("score")
        
# print(get_score("Patricia"))
# print(f"{courses}")

def get_first_letter(letter:str) -> int:
    counter = 0
    for student in courses:
        if student.get("name")[0].lower() == letter.lower():
            counter += 1
    return counter

# print(get_first_letter("p"))

'''
let counter = 0;
for (student of courses) {
    if (student.name[0] === "P") {
        counter ++;
    };
};
return counter;
'''

# best_student = None
def highest_score(is_max=True):
    best_score = 0 if is_max else 10
    for student in courses: # student = courses[i]
        if is_max:
            if student["score"] > best_score:
                best_score = student["score"]
                best_student = student
        else:
            if student["score"] < best_score:
                best_score = student["score"]
                best_student = student
    return best_student["name"]
print(highest_score(is_max=False))
# print("END")

# Big O notation -> O(n*2) -> O(n)