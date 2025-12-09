with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

# raw_input_lines=[
# '987654321111111',
#  '811111111111119',
#  '234234234234278',
#  '818181911112111'
#   ]
max_values = []
length = 12
for raw_line in raw_input_lines:
  line = raw_line.strip()
  print(f"line is {line}")
  current_char = 0
  max_voltage_str = ""
  remaining_line = line
  start_index_offset = 0
  for i in range(length):
    start_index = start_index_offset
    end_index = -length + i + 1
    print(start_index, end_index, line)
    if end_index:
      section_of_interest = line[start_index:end_index]
    else:
      section_of_interest = line[start_index:]
    print(f"Looking for the {i+1} character.  Considering segment {section_of_interest}")
    for digit_to_seek in range(9, -1, -1):
      print(f"  looking for a {digit_to_seek}")
      found_char_index = section_of_interest.find(str(digit_to_seek))
      if found_char_index != -1:
        max_voltage_str += section_of_interest[found_char_index]
        print(f"  Found {i} digit.  Value is {section_of_interest[found_char_index]}.  Current string is {max_voltage_str} with length {len(max_voltage_str)}")
        start_index_offset += found_char_index + 1
        break
  print(f"Found string {max_voltage_str}")
  max_values.append(int(max_voltage_str))
for i in max_values:
  print(i)
print(sum(max_values))

