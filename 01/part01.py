with open('input.txt', 'r') as f:
  turns = f.readlines()

# turns = ['L68',
# 'L30',
# 'R48',
# 'L5',
# 'R60',
# 'L55',
# 'L1',
# 'L99',
# 'R14',
# 'L82',]

positions = [50]
for line in turns:
  index = int(line[1:])
  if line[0] == "R":
    direction = 1
  else:
    direction = -1
  new_position = (positions[-1] + direction * index) % 100
  positions.append(new_position)
print(positions)
print(positions.count(0))

