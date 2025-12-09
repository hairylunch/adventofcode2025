with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

# raw_input_lines=['987654321111111',
# '811111111111119',
# '234234234234278',
# '818181911112111']


max_values = []
print(raw_input_lines)
for line in raw_input_lines:
  max_voltage = 0
  for position, value in enumerate(line):
    for j in line[position+1:]:
      v = int(value+j)
      if v > max_voltage:
        max_voltage = v
  max_values.append(max_voltage)
print(max_values)
print(sum(max_values))
