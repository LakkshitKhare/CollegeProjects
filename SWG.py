import random as r
name = input("Enter Your name\n")
namen= name.capitalize()
print("""Enter the number according to the following:
1. Snake
2. Water
3. Gun""")
print("First to 5 Match!!")
i=0
u=0
c=0
while(c<5 and u<5):
  listed = [1,2,3]
  a = r.choice(listed)
  b = int(input("Enter a choice\n"))
  
  match(b):
   case 1:
    print("Your choice was Snake ")
    if (a==b):
       print("No one won") 
    if (a==2):
      print("You won yay")
      u=u+1  
    if (a==3):
      print("Bot won!!")
      c=c+1
    print(f"The score is {u}-{c}")
   case 2:
     print("Your choice was Water ")
     if(a==1):
       print("I won!!")
       c=c+1
     if (a==b):
       print("No one won!!")
     if (a==3):
       print("You won!!")
       u=u+1
     print(f"The score is {u}-{c}")
     
   case 3:
     print("Your choice was Gun ")
     if(a==1):
       print("Ah u won!")
       u=u+1
     if (a==2):
       print("Yay bot won!!")
       c=c+1
     if (a==b):
      print("No one won!!")
     print(f"The score is {u}-{c}")  
   case default:
    print("Enter a valid choice")
    break;
  
  i=i+1
  

print(f"You got {u} points and I got {c} points")
if (u==c):
  print("Tie match")
if (u>c):
  print(f"{namen} won")
if (u<c):
  print(f"Bot won against {namen}")
