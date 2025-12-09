with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

raw_input_lines=[
'3-5',
'10-14',
'16-20',
'12-18',
'',
'1',
'5',
'8',
'11',
'17',
'32',
]

fresh_pairs = []
for line in raw_input_lines:
  if "-" in line:
    raw_left, raw_right = line.strip().split("-")
    left = int(raw_left)
    right = int(raw_right)
    overlapping = False
    for pair in fresh_pairs:
      # if pair[0] <= left <= pair[1] and right > pair[1]:
      if pair[0] <= left <= pair[1] < right:
        pair[1] = right
        overlapping = True
        continue
      elif left < pair[0] <= right <= pair[1]:
        pair[0] = left
        overlapping = True
        continue
    if not overlapping:
      fresh_pairs.append([left, right])
    print(f"Parse {line}, currently {fresh_pairs}")

# re parse to look for intersecting groups
old_pairs = fresh_pairs
new_pairs = []
while old_pairs != new_pairs:
  new_pairs = []
  for i, pair in enumerate(old_pairs):
    left = pair[0]
    right = pair[1]
    for j, pair_to_check_against in enumerate(old_pairs):
      if i != j:
        # print(i,j,pair, pair_to_check_against)
        if pair_to_check_against[0] <= left <= pair_to_check_against[1] < right:
          new_pairs.append([pair_to_check_against[0], right])
          continue
        elif left < pair_to_check_against[0] <= right <= pair_to_check_against[1]:
          new_pairs.append([left, pair_to_check_against[1]])
          continue
        else:
          if [left, right] not in new_pairs:
            new_pairs.append([left, right])
        print(new_pairs)
  print(f"After the loop {old_pairs}, {new_pairs}")
print(new_pairs)
# too high
# 29540887973767680
