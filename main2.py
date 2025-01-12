#importing the required modules
import openpyxl
import random
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font

#Reading teacher's data from file
teacher_data = {}
with open("teachers.txt", 'r') as teachers_data_file:
    for  line in teachers_data_file:
        line = line.strip("()\n")
        name, subject = line.split("(")
        teacher_data[name.strip()] = subject.strip()
# print(teacher_data) --> for testing purpose

#Extracting data of subject and teachers
subject = list(set(teacher_data.values()))
teachers = list(teacher_data.keys())
# print(subject)  --> For testing purpose
# print(teachers) --> For testing purpose

#creating data of absent teachers
absent_teacher =  input("Enter names of absent teachers (separate by commas if many): ").split(",")
absent_teacher = [name.strip() for name in absent_teacher]
#print(absent_teacher) --> For testing purpose

#removing the absent teachers from the list of teachers
teachers = [teacher for teacher in teachers if teacher not in absent_teacher]
# print(teachers) --> for testing purpose

#generating a random light color code
def generate_light_color():
    r = random.randint(200,255)
    g = random.randint(200,255)
    b = random.randint(200,255)
    
    return f"{r:02X}{g:02X}{b:02X}"
# print(generate_light_color()) --> for testing purpose

#Assigning colors to subjects and teachers
subject_colors = {subjects: generate_light_color() for subjects in subject}
teacher_colors= {teacher: subject_colors[teacher_data[teacher]] for teacher in teachers}
# print(subject_colors) --> for testing purpose
# print(teacher_colors) --> for testing purpose 

#Defining classes, sections, and periods
classes = [
    "9A", "9B", "9C", "9D",
    "10A", "10B", "10C", "10D",
    "11A", "11B",
    "12A", "12B",
]
num_periods = 8
max_periods_per_teacher = 7

#Initialing table and tracking the data
