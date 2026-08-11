import ast

students = []

class student:
    def __init__(self,roll,name,marks):
        self.roll = roll
        self.name = name
        self.marks = marks


    def total(self):
        return sum(self.marks)

    def percentage(self):
        return sum(self.marks)/5


    def display(self):
        print(f"Roll No. : {self.roll}")
        print(f" Name : {self.name}")
        print(f" Marks   :{self.marks}")
        print(f" percentage  :{self.percentage()}")
        print(f" total  : {self.total()}")


def load_student():
    students = []
    try:
        with open("student.txt", "r") as file :
            for line in file:
                line =line.strip()
                if line:
                    roll,name,marks = line.split(",",2)
                    roll = int(roll)
                    marks = ast.literal_eval(marks)
                    stud = student(roll,name,marks)
                    students.append(stud)
    except FileNotFoundError :
        pass
    return students
students =load_student()

    
def add_student():
    n = int(input("enter no. of student you want to add   :"))
    for i in range(n):
        roll = int(input("enter student roll number    :"))
        name = input("enter student name   :")
        mark1 = float(input("enter mark of 1st subject   :"))
        mark2 = float(input("enter mark of 2st subject   :"))
        mark3 = float(input("enter mark of 3st subject   :"))
        mark4 = float(input("enter mark of 4st subject   :"))
        mark5 = float(input("enter mark of 5st subject   :"))
        mark = [ mark1,mark2,mark3,mark4,mark5]
    
        for s in students :
            if s.roll == roll :
                print("roll number already exist")
                return
        new_student =student(roll , name , mark)
        students.append(new_student )
        print(" new student is added  successfully")
    

def view_students():
    for s in students:
        s.display()

def search_student():
    roll = int(input("enter roll no. you want to search  :"))
    for s in students:
        if s.roll == roll:
            s.display()
            return

    print("not found")
            

def delete_student():
    roll = int(input(" enter roll no. you want to delete   :"))
    for s in students:
        if s.roll == roll:
            students.remove(s)
            print("deleted successfully")
            return
        
    print("not found")
            

def update_student():
    roll = int(input("enter roll no. you want to update   :"))
    for s in students:
        if s.roll == roll:
            name = input("enter student name   :")
            mark1 = float(input("enter mark of 1st subject   :"))
            mark2 = float(input("enter mark of 2st subject   :"))
            mark3 = float(input("enter mark of 3st subject   :"))
            mark4 = float(input("enter mark of 4st subject   :"))
            mark5 = float(input("enter mark of 5st subject   :"))
            mark = [mark1,mark2,mark3,mark4,mark5]
            s.name = name
            s.marks = mark
            
            print("student data updated successfully")
            return
    print("not found")
        
        
            

def save_data():
    with open("student.txt","w") as file:
        for s in students:
            file.write(f"{s.roll},{s.name},{s.marks}\n")
    print("data saved")
              




while True:

    print("1.add_student")
    print("2.view_students")
    print("3.search_student")
    print("4.delete_student")
    print("5.update_student")
    print("6.exit")

    choice = int(input("enter choice  :"))
    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        update_student()

    elif choice == 6 :
        save_data()
        print("thanks for coming")
        break