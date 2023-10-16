class student:
    nm=""
    rlno=""
    cgpa=0.0
    def __init__(self):
        self.nm=input("\nUr Name: ")
        self.rlno=input("Ur Roll No.:  ")
        self.cgpa=float(input("Ur CGPA Point: "))

def sort_student(*n):
    return (sorted(n,key=lambda student: student.cgpa,reverse=True))
    
t=[]

for i in range(int(input("Enter no.of data contain a list: "))):
	t.append(student())

print("\nData Before Sorting,\n")
for i in t:
	print("Name: ",i.nm,"\tRoll No.: ",i.rlno,"\tCGPA: ",i.cgpa)


print("\nData After Sorting,\n")
for i in sort_student(*t):
	print("Name: ",i.nm,"\tRoll No.: ",i.rlno,"\tCGPA: ",i.cgpa)

