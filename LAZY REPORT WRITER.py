import random 

Students = int(input("number of students :" ))
Choose_Comment = ["Improve handwriting", "Elaborate on this point", "Why?", "Explain further", "What else could this suggest?"]
for i in range (Students) : 
  chosen = random.choice(Choose_Comment)
  print(chosen) 
