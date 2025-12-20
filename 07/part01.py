with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

beams = set()
split_count = 0
for i, line in enumerate(raw_input_lines):
  if i == 0:
    start = line.find('S')
    beams = {start}
  else:
    print(line, beams)
    for j, char in enumerate(line):
      print(f"  {i}, {j}, {char}")
      if j in beams and char == '^':
        split_count += 1
        beams.remove(j)
        beams.add(j-1)
        beams.add(j+1)

print(split_count)
