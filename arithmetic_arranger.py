def arithmetic_arranger(problems, answ=False):
  # checking no of problems
  n_problems = len(problems)
  if n_problems > 5:
    return("Error: Too many problems.")
  # arrays
  operand_a = []
  operand_b = []
  operator = []
  solution = []
  
  # parsing and solving
  for i in problems:
    if '+' in i:
      n = i.split(" + ")
      operand_a.append(n[0])
      operand_b.append(n[1])
      operator.append("+")
      if n[0].isnumeric() == False:
          return "Error: Numbers must only contain digits."
      elif n[1].isnumeric() == False:
          return "Error: Numbers must only contain digits."
      solution.append(int(n[0])+int(n[1]))
    elif '-' in i:
      n = i.split(" - ")
      operand_a.append(n[0])
      operand_b.append(n[1])
      operator.append("-")
      if n[0].isnumeric() == False:
          return "Error: Numbers must only contain digits."
      elif n[1].isnumeric() == False:
          return "Error: Numbers must only contain digits."
      solution.append(int(n[0])-int(n[1]))
    else:
      return "Error: Operator must be '+' or '-'."
  
  # output parameters
  lengths = []
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  
  #formatting output
  for i,j in zip(operand_a,operand_b):
    if len(str(i)) >= len(str(j)):
      lengths.append(len(str(i)) + 2)
    else:
      lengths.append(len(str(j)) + 2)
     
  #checking lengths
  for i in lengths:
    if i > 6:
      return "Error: Numbers cannot be more than four digits."
      
  for i in range(0,n_problems):
    line1 = line1 + " " * (lengths[i]-len(operand_a[i])) +  f"{operand_a[i]}" + " " * 4
    line2 = line2 + f"{operator[i]}" + " " * (lengths[i]-len(operand_b[i])-1) + f"{operand_b[i]}" + " " * 4
    line3 = line3 + "-" * lengths[i] + " " * 4
    line4 = line4 + " " * (lengths[i]-len(str(solution[i]))) +  f"{solution[i]}" + " " * 4

  # another useless addition that is necessary too pass automated fcc testing
  line1 = line1.rstrip()
  line2 = line2.rstrip()
  line3 = line3.rstrip()
  line4 = line4.rstrip()

  if answ == True:
     arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
  else:
     arranged_problems = line1 + "\n" + line2 + "\n" + line3    
  return arranged_problems