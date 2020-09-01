import random 

name = str(input("name :"))
Choose_Insult = ["Too bad you can't photoshop your ugly personality", "So if i type 'idiot' into Google, would your picture come up?", "Someday you'll go far, and I hope you stay there"]
for i in range(1,3) : 
    chosen = random.choice(Choose_Insult)
    print (name,",", chosen)
    Choose_Insult.remove(chosen)
