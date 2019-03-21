def calc_add(a, b):
  return a+b

def calc_subtract(a, b):
  return a-b

def calc_multiple(a, b):
  return a*b

def calc_divide(a, b):
  return a / b 
def check_operation_name(operation):
  while True:
    pass

method_dict = {
  "dodawanie" : calc_add,
  "odejmowanie" : calc_subtract,
  "mnozenie" : calc_multiple,
  "dzielenie" : calc_divide
}

if __name__ == "__main__":
  print("Witam w moim kalkulatorze :P")
  operation = input("Podaj dzialanie: dodawanie, odjemowanie, mnozenie lub dzielenie: ")
  print(operation)
