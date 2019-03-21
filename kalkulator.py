def calc_add(a, *args):
  print("{} + {} = ".format(str(a), args), end = " ")
  list_args = args[0].strip(" ").split(" ")
  print(args)
  return a + sum([int(i) for i in list_args])

def calc_substract(a, b):
  print("{} - {} = ".format(str(a), str(b)), end = " ")
  return a-b

def calc_multiple(a, b):
  print("{} * {} = ".format(str(a), str(b)), end = " ")
  return a*b

def calc_divide(a, b):
  print("{} : {} = ".format(str(a), str(b)), end = " ")
  try:
    return a / b 
  except ZeroDivisionError:
    print("Nie dziel przez ZERO!")
    return "3 = 4"

def check_operation_name(operation):
  if operation in method_dict:
    return method_dict[operation]
  operation = input("Niepoprawne dzialanie, podaj jeszce raz: dodawanie, odjemowanie, mnozenie lub dzielenie: ")
  check_operation_name(operation)


method_dict = {
  "dodawanie" : calc_add,
  "odejmowanie" : calc_substract,
  "mnozenie" : calc_multiple,
  "dzielenie" : calc_divide
}

if __name__ == "__main__":
  print("Witam w moim kalkulatorze :P")
  while True:
    operation = input("Podaj dzialanie: dodawanie, odjemowanie, mnozenie lub dzielenie: ")
    if operation == "exit":
      break
    operation_def = check_operation_name(operation)
    a = (input("Podaj pierwsza liczbe: "))
    b = (input("Podaj druga liczbe: "))
    print(operation_def(int(a), int(b))
