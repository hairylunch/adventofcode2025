import math

with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

parsed_input = []
operations = []
for i, line in enumerate(raw_input_lines):
  if i != len(raw_input_lines) - 1:
    parsed_input.append(list(map(int, line.split())))
  else:
    operations = line.split()
print(parsed_input)

answers = []

for col in range(len(parsed_input[0])):
  operation = operations[col]
  values = [x[col] for x in parsed_input]
  if operation == '+':
    output = sum(values)
  elif operation == '*':
    output = math.prod(values)
  answers.append(output)

print(sum(answers))



