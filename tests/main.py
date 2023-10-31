from os import system
from examinator import Examinator
from utils import menu, print_questions, list_questions
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
        
        questions = print_questions(exam)
        count = questions["count"]
        incorrects = questions["incorrects"]
            
        print(f"{count}/{limit}")
        list_questions(incorrects)
        input(": ")

    elif user == "2":
        print("PCAP")
        ex_1 = Examinator("questions_clean.json", limit=limit, filter_dict={"family": "pcap"})
        exam = ex_1.exam
        
        questions = print_questions(exam)
        count = questions["count"]
        incorrects = questions["incorrects"]
            
        print(f"{count}/{limit}")
        list_questions(incorrects)
        input(": ")

print("Bye!")