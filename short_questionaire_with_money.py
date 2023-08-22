print ("Welcome to KBC python version")
print ("""Rules to This game
1. You have to Answer all the questions 
2. You cannot quit in Between
3. Final prize would be given at last
4. If u answer a question wrongly no money would be deducted
5. All the answers should be given in respected manner
5. Enjoy""")
name = input("Enter Your name Sir/ma'am \n ")
naam = name.capitalize()
question = ("Who is the president of India", "Who was the 1st female president of India", "Who was the 1st female Prime minister of india", "Who wrote the national anthem of India","What is the Capital Of India")
answers = ("Draupadi Murmu", "Pratibha Patil", "Indira Gandhi", "Rabindranath Tagore", "New Delhi")
n = 0
p = 0
rs = 0
correct = 0
wrong = 0
for quest in question[n] :

  while (n<5) and (p<5):
    print ("Question Number",n+1,"is:\n")
    print (question[n])
    n = n+1
    user = input("Enter your answer \n")
    
    if (user == answers[p]):
      print("Correct answer + 1000 rs added\n")
      rs = rs + 1000
      correct = correct + 1
    else :
      print ("Sorry Wrong answer")
      wrong = wrong+1
    p = p +1 


print ("Woohoo!!! You have sucessfully completed the KBC pyhton version")
print ("The number of coorect answers u did were: ", correct)
print ("The number of wrong answers u did were :", wrong)
print ("Ths sum of Rupees ", naam , "would be taking home with itself is :",rs,"Rupees")



