print("welcome to the departmental store")
print("please enter your name")
name=input()
print("welcome,",name)
print("which department would you like to visit")
print("1 grocery")
print("2 electronics")
print("3 household items")
choice=int(input())

if choice== 1:
  print("welcome to the grocery department")
  print("which product would you like to buy")
  print("1 fruits")
  print("2 vegetables")
  item1=int(input())

  if item1== 1:
    print("thanks for choosing")
    print("which fruit would you like to buy")
    print("1 apple")
    print("2 banana")
    print("3 mango")
    print("4 papaya")

    item=int(input())
    if item== 1:
      print("thanks for choosing")
      print("the price of apple is rupee12 per 1 kilogram")
      print("please type how much apple would you by in kilograms")
      amount=float(input())
      total=amount*12
      total=round(total,3)
      print("total amount=rupees",total)
      print("thanks for buying our team will contact you as soon as possible")
    
    elif item== 2:
      print("thanks for choosing")
      print("the price of banana is rupee12 per dozen")
      print("please type how much banana would you by in dozens")
      amount2=float(input())
      total=amount2*12
      total=round(total,3)
      print("total amount=rupees",total)
      print("thanks for buying our team will contact you as soon as possible")

    elif item== 3:
      print("thanks for choosing")
      print("the price of mango is rupee12 per 100 gram")
      print("please type how much mango would you by in grams")
      amount=float(input())
      total=amount*0.12
      total=round(total,3)
      print("total amount=rupees",total)
      print("thanks for buying our team will contact you as soon as possible")
    
    elif item== 4:
      print("thanks for choosing")
      print("the price of papaya is rupee12 per kilogram")
      print("please type how much papaya would you by in kilogram")
      amount=float(input())
      total=amount*12
      total=round(total,3)
      print("total amount=rupees",total)
      print("thanks for buying our team will contact you as soon as possible")
    
    else:
     print("invalid attempt")

  elif item1== 2:
    print("thanks for choosing")
    print("which vegetable would you like to buy")
    print("1 potato")
    print("2 tomato")
    print("3 cauliflower")
     
    choice2=int(input())
    if choice2== 1:
      print("thanks for choosing")
      print("the price of potatoes is rupees10 per kilogram ")
      print("please tell what amount of potatoes you would buy in kilograms")
      amount=float(input())
      total=amount*12
      total=round(total,3)
      print("your total amount is rupees",total)
      print("thanks for buying our team would contact you as soon as possible")

    elif choice2== 2:
      print("thanks for choosing")
      print("the price of tomatoes is rupees15 per kilogram ")
      print("please tell what amount of tomatoes you would buy in kilograms")
      amount=float(input())
      total=amount*15
      total=round(total,3)
      print("your total amount is rupees",total)
      print("thanks for buying our team would contact you as soon as possible")

    elif choice2== 3:
      print("thanks for choosing")
      print("the price of cauliflowers is rupees50 per kilogram ")
      print("please tell what amount of cauliflower you would buy in kilograms")
      amount=float(input())
      total=amount*50
      total=round(total,3)
      print("your total amount is rupees",total)
      print("thanks for buying our team would contact you as soon as possible")

    else:
      print("invalid attempt")

elif choice== 2:
  print("welcome to the electronics department")
  print("which product would you buy")
  print("1 phone")

  choice3=int(input())
  
  if choice3== 1:
   print("thanks for choosing")
   print("which company phone would you like to buy")
   print("1 iphone")
   print("2 samsung")

  item=int(input())

  if item== 1:
    print("the price of an iphone is rupees100000")
    print("your total is rupees 100000")
    print("thanks for purchasing,our team will contact you as soon as possible")

  elif item== 2:
    print("the price of an samsung is rupees50000")
    print("your total is rupees 50000")
    print("thanks for purchasing,our team will contact you as soon as possible")

  else:
    print("invalid choice")

elif choice== 3:
  print("welcome to the household items department ")
  print("what do you want to buy")
  print("1 utensils")
  print("2 soaps")

  itemm=int(input())

  if itemm==1:
    print("thanks for buying utensils,the price of 1 utensil is rupees 1000")
    print("how many utensils do you want to buy")
    hello=int(input())
    amount=hello*1000
    print("your total is rupees",amount)
    print("thanks for buying,our team will reach you as soon as possible")

  elif itemm==2:
    print("thanks for buying soaps,the price of 1 soap is rupees 500")
    print("how many soaps do you want to buy")
    hello=int(input())
    amount=hello*500
    print("your total is rupees",amount)
    print("thanks for buying,our team will reach you as soon as possible")
  
  
    

    
    
