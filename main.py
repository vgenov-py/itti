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
},
{
	"name": "Patricia",
	"id" :  "007",
  "score": 2.3
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
def highest_score():
    best_score = 0
    for student in courses: # student = courses[i]
        if student["score"] > best_score:
            best_score = student["score"]
            best_student = student
    return best_student
print(highest_score())
print("END")

# Big O notation -> O(n*2) -> O(n)