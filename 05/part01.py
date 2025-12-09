with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

fresh_pairs = []
available_and_fresh = set()
for line in raw_input_lines:
  if "-" in line:
    raw_left, raw_right = line.strip().split("-")
    fresh_pairs.append([int(raw_left), int(raw_right)])

for line in raw_input_lines:
  if line != "\n" and not "-" in line:
    ingredient = int(line.strip())
    for pair in fresh_pairs:
      if pair[0] <= ingredient <= pair[1]:
        available_and_fresh.add(ingredient)
        continue


print(available_and_fresh)
print(len(available_and_fresh))

# fresh_ingredients = set()
# available_and_fresh = set()
# for line in raw_input_lines:
#   if line:
#     raw_left, raw_right = line.strip().split("-")
#     for i in range(int(raw_left), int(raw_right)+1):
#       fresh_ingredients.add(i)
#   else:
#     break
#
# for line in raw_input_lines:
#   if line and not "-" in line:
#     if int(line.strip()) in fresh_ingredients:
#       available_and_fresh.add(line)
#
# print(available_and_fresh)
# print(len(available_and_fresh))

