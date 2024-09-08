print("Insert Your card")
pin =1234
bal = 20000
ent_pin = int(input("Enter Your pin"))
while True:
  if ent_pin == pin:
    print("""Select from the below options
    1 . Check Your balance
    2 . Withdraw cash
    3 . Deposit cash
    4 . Reset Pin
    5 . Cancel """)
    opt = int(input("Enter the option You want to use: "))
    match opt:
      case 1:
        print("Your account balance is ", bal)
      case 2:
        wit_am = int(input("Enter the amount you want to    withdraw"))
        if wit_am<bal:
          bal = bal-wit_am
          print("New balance is",bal)
        else:
          print("Insufficient balance. Please try again.")
          exit
      case 3:
        dep_am = int(input("Enter the amount You want to deposit"))
        bal = bal+dep_am
        print("New balance is ",bal)
      case 4:
        r_pin = int(input("Enter Your last pin"))
        if r_pin == pin:
          n_pin=int(input("Enter Your new pin"))
          pin = n_pin
          print("Your new pin is set and it is **** ")
          
        else:
          print("Wrong last pin")
          exit
      case 5:
        exit
        break
      case default:
        print("Enter a valid choice")
        break
        
        
  else:
    print("Wrong pin")
    exit
