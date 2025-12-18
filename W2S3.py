#score =int(input("Enter score"))
#if score >= 70:
 #   print("distinction")
#elif score >= 40:
 #   print("pass")
#else:
#   print("fail"):

 #cinema ticket category
#age= int(input("enter age"))

#if age <5:
 #   print ("free entry")
#elif 5 < age < 18:
 #    print("child ticket")
#elif 18 <= age <= 64:
 #    print("adult ticket")
#else:
 #    print("senior ticket")

 #2 library fine calculator
#days_late= int(input("enter days late"))
#if days_late <= 0:
 #   print("no fine")
#elif 1 <= days_late <= 5:
 #   print("fine =£1")
#elif 6 <= days_late <= 10:
 #   print("fine £5")
#else:
 #   print("fine =£10 and membership review")

 #3 exam borderline check
#score =int(input("enter number between 0-100 "))
#if score >=38:
 #   if score >38 and score <42:
  #      print("borderline pass,consider review")
   # else:
    #    print("pass")
#else:
 #   print("fail")

#4 Discount Eligibility
#is_student= (input("are you a student(yes/no:"))
#age =int(input("enter your age:"))
#if is_student == "yes" or age <18:
 #   print("discount applied")
#else:
 #   print ("no discount")
"""
#5 Traffic light
colour =(input("show the colour"))
if colour =="red":
    print("stop")
elif colour =="amber":
    print("get ready")
elif colour == "green":
    print("Go")
else:
    print("invalid colour")
"""

#6 multiple of 3,5 or both
#number =int(input("enter number"))
#if (number % 3) == 0 and (number % 5) == 0:
 #   print("fizzBuzz")
#elif (number % 3) ==0:
 #   print("fizz")
#elif (number % 5) == 0:
 #   print("Buzz")
#else :
 #   print("no match")
"""
 #7 Meal recommendations
time_of_day =(input("enter the time of day "))
is_hungry= (input("are you hungry"))

if is_hungry =="no":
    print("have some water")
elif is_hungry == "yes":
    if time_of_day =="morning":
        print("have breakfast")
    elif time_of_day=="afternoon":
        print("have lunch")
    elif time_of_day=="evening":
        print("have dinner")
    else:
        print("snack time")
"""
"""
#8module mark status
coursemark =int(input("enter mark between 0-100"))
exammark =int(input("enter exam mark 0-100" ))
if coursemark <35 or exammark <35:
    print("fail")
elif coursemark >= 40 and exammark >= 40:
    print("module passed")
else:
    print("module failed")
"""
"""
#9 simple two-stage Verification
pin=int(input("enter your pin"))
if pin ==1234:
    colour=(input("what is your favorite colour")).lower()
    if colour == "blue":
        print("access granted")
    else:
        print("security answer incorrect")
else:
    print("pin wrong")
"""
#10 sport suggestion by weather and mood
#weather= (input("enter weather condition"))
#mood =(input("enter mood"))
#if weather =="sunny":
    #if mood=="active":
   #     print("go for a run")
  #  if mood=="tired":
 #       print("relax in the park")
#elif weather=="rainy":
 #   print("indoor workout")
#elif weather =="cold":
 #   print("go to the gym")
#else:
   # print("no suggestion")