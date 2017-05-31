import pythagore
problem_type = input("Type 1 for right triangle checker. Type 2 for hypotenuse calc. for right triangle. Type 3 for missing arm value calc. for right triangle. Type 4 for volume of a cylinder calc. Type 5 for cone volume calc. Type 6 for volume of a sphere calc.")
if problem_type == "1":
  pythagore.check()
elif problem_type == "2":
  a = input("a=")
  b = input("b=")
  a = float(a)
  b = float(b)
  a = a ** 2
  b = b ** 2
  print("the hypotenuse is" , (a + b) ** 0.5 , "and a and b squared equal" , a , "and" , b)
elif problem_type == "3":
  a = input("a=")
  c = input("c=")
  a = float(a)
  c = float(c)
  a = a ** 2
  c = c ** 2
  b = c - a
  b = b ** 0.5
  print("the missing arm value is" , b , "and a and c squared are" , a , "and" , c)
elif problem_type == "4":
  a = input("radius=")
  b = input("height=")
  a = float(a)
  b = float(b)
  circle_area = a ** 2 * 3.14
  print("the volume is" , circle_area * b)
elif problem_type == "5":
  a = input("radius=")
  b = input("height=")
  a = float(a)
  b = float(b)
  circle_area = a ** 2 * 3.14
  volume = circle_area * b / 3
  print("the volume is" , volume , "and the base area is" , circle_area)
elif problem_type == "6":
  a = input("radius=")
  a = float(a)
  a = a ** 3
  a = a * 3.14
  a = a * 4
  a = a / 3
  print("The volume is about" , a)
else:
  yes = True
  while yes:
    print("That is not a valid function")
