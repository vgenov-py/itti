from os import system
from examinator import Examinator

user = ""
limit = 1

def menu():
    system("clear")
    print("1. PCEP")
    print("2. PCAP")
    print("Q. Exit")

while user.upper() != "Q":
    menu()
    user = input(": ")

    if user == "1":
        ex_1 = Examinator("questions_clean.json", limit=limit, filter_dict={"family": "pcep"})
        exam = ex_1.exam
        count = 0
        incorrects = []
        print("EXAMEN: ")
        for question in exam: # O(n)
            system("clear")
            print("-".center(50, "-"))
            print(question["question"])
            print("-".center(50, "-"))
            for i, option in enumerate(question["options"]): # O(1) 
                print(f"{i+1}: {option}")
            
            to_append = {   
                "question": question["question"],
                "correct_answer": question["answer"]
            }

            try:
                user_answer = int(input(": ")) - 1
                user_answer = question["options"][user_answer]
                if user_answer == question["answer"]:
                    count += 1
                to_append["user_answer"] = user_answer
            except ValueError:
                to_append["user_answer"] = "Sin contestar"
            except IndexError:
                to_append["user_answer"] = "Sin contestar"
            incorrects.append(to_append)
            
        print(f"{count}/{limit}")
        for question in incorrects:
            for k,v in question.items():
                print(f"{k}: {v}")
        input(": ")

    elif user == "2":
        print("PCAP")

print("Bye!")