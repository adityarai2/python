first = input("enter first number")
operator = input("enter operator(+,-,*,/,%) :")
seceond = input("enter seceond number:")
first = int(first)
seceond = int(seceond)
if operator == "+":
 print(first+seceond)
elif operator == "-":
 print(first-seceond)
elif operator == "*":
 print(first*seceond)
elif operator == "/":
  print(first/seceond)
elif operator == "%":
   print("first%")
else:
  print("invalid operation")
  