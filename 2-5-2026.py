# create a list of dict to stores student records

# initial data

students=[{"id":101,"name":"alice","score":85},
          {"id":102,"name":"bob","score":78},
          {"id":103,"name":"charlie","score":92}

]


# print the name of each student using a loop

print("student names:")

for s in students:
    print(s["name"])

#print the average score of all students

total=0

for s in students:
  total+=s["score"]

avg=total/len(students)
print("\n average score",avg)

# add a new student in list

students.append ({"id":104,"name":"john","score":75})

print("student list :", students)

# update the score of a student with id 102 to 88

for s in students:
    if s["id"]:
     s["score"]=88

print("students list:",students)



# delete the record of the student named"charlie"
new_list=[]

for s in students:
      if s ["name"]=="charlie":
       new_list.append(s)

students=new_list
print ("students list:",students)

#print names of students who scored more than 80.

for s in students:
    if s ["score"]<80:
        print(s["name"])


# sort the list of students by score (descending)

def get_score (students):
    return students["score"]

students.sort(key=get_score,reverse=True)

print ("\n sorted by score (Desc):")

for s in students:
    print(s)

# find the students with heighest score

max_score=max(s["score"] for s in students)

top_student=[]


top_student=[s for s in students if s["score"]==max_score]



# use a loop to create a report in this format:

#name:alice|score : 85|grade : b

#(add grading logic:a=90+,b=80-89,c=<80)

print("students Report:")

def get_report (score):

    if score>=90:
        return"a"
    elif score>=80:
        return "b"
    else:
        return"c"

for s in students:
    grade=get_report(s["score"])
    print("name",s["name"],"|score:",s["score"],"|grade:",grade)


# count how many students got each grade

grade_count={"a":0,"b":0,"c":0}

for s in students:
    grade=get_report(s["score"])
    grade_count [grade]+=1

print("\n grade count:",grade_count)
