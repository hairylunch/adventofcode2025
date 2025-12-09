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

i = 0
positions = [50]
count = 0
for line in turns:
  index = int(line[1:])
  if line[0] == "R":
    direction = 1
  else:
    direction = -1
  temp_new_position = positions[-1] + direction * index
  new_position = temp_new_position % 100

  if temp_new_position <= 0 and positions[-1] != 0:
    count += 1

  count += abs(int(temp_new_position/100))

  positions.append(new_position)
  i += 1
  print(i, line.strip(), count, temp_new_position, new_position)


print(count)
#2742 Too low
#6492 too high
# 6054 wrong
