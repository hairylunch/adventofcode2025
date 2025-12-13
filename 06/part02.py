import math

def cephalapod_math(numbers, operation):
  if operation == '+':
    output = sum(numbers)
  elif operation == '*':
    output = math.prod(numbers)
  return output

with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

# raw_input_lines = [
#   '123 328  51 64 ',
#   ' 45 64  387 23 ',
#   '  6 98  215 314',
#   '*   +   *   +  ',
# ]

# read by columns
col_count = len(raw_input_lines[0])

answers = []
numbers = []
operation = ''
for i in range(col_count):
  digit_string = ''

  for row, line in enumerate(raw_input_lines):
    if row != len(raw_input_lines) - 1:
      digit_string += line[i]
    else:
      operation += line[i]
  # print(i, digit_string, operation )
  if digit_string.isspace():
    print(numbers, operation.strip())
    # This is where we need to get the operation and do the math
    answers.append(cephalapod_math(numbers, operation.strip()))
    # reset things
    numbers = []
    operation = ''
  elif i == col_count-1:
    numbers.append(int(digit_string.strip()))
    answers.append(cephalapod_math(numbers, operation.strip()))
  else:
    numbers.append(int(digit_string.strip()))
print(answers)
print((sum(answers)))
