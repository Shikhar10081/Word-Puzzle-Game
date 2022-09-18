import random
score=0
q="Word Puzzle Game"
print(q.center(80,"*"))
print("  ***Given the user score +1 if ans is  correct else -1***")
print(" ")
lis=['''"RAEHTF"''' ,'''"KABRE"''', '''"BLCAK"''','''"RENEG"''','''"OAERELANP"''']
LIS2=["FATHER","BREAK","BLACK","GREEN","AEROPLANE"]

print("Arrange the letters to form a valid word :) ="+random.choice(lis))   #1st
x=str(input("Enter correct world: = "))
if x in LIS2:
    print("correct")
    score+=1
else:
    print("wrong")
    score-=1              #1s end
print("Arrange the letters to form a valid word :) "+random.choice(lis))  #2nd 
a=str(input("Enter correct world: = "))
if a in LIS2:
    print("correct")
    score+=1
else:
    print("wrong")
    score-=1        #2nd  end
print("Arrange the letters to form a valid word :)= "+random.choice(lis))   #3 rd
x=str(input("Enter correct world: = "))
if x in LIS2:
    print("correct")
    score+=1
else:
    print("wrong")
    score-=1            #3 end
print("Arrange the letters to form a valid word :) ="+random.choice(lis))     #4th
x=str(input("Enter correct world: = "))
if x in LIS2:
    print("correct")
    score+=1
else:
    print("wrong")
    score-=1   #4 end
print("The random word is: ="+random.choice(lis))   #5th 
x=str(input("Enter correct world: = "))
if x in LIS2:
    print("correct")
    score+=1
else:
    print("wrong")
    score-=1       # 5th end
g="Game End   Thanks for playing game :)"
print(g.center(80,"*"))
print("Arrange the letters to form a valid word :) = ",score)
if score<4:
    print("******Better Luck Next Time*******")
else:
    ("         ****YOU ARE GREAT****")
    
    
    
    
    
    
