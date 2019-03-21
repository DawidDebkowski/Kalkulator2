def calc_add(a, b):
  return a+b

def calc_substract(a, b):
  return a-b

def calc_multiple(a, b):
  return a*b

def calc_divide(a, b):
  return a / b 
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
  operation = input("Podaj dzialanie: dodawanie, odjemowanie, mnozenie lub dzielenie: ")
  operation_def = check_operation_name(operation)
  a = int(input("Podaj pierwsza liczbe: "))
  b = int(input("Podaj druga liczbe: "))
  print(operation_def(a, b))
