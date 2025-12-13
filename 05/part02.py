with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

# raw_input_lines=[
# '3-5',
# '10-14',
# '16-20',
# '12-18',
#  '10-20',
#   '3-5',
# '',
# '1',
# '5',
# '8',
# '11',
# '17',
# '32',
# ]

def main():
  fresh_pairs = []
  for line in raw_input_lines:
    if "-" in line:
      raw_left, raw_right = line.strip().split("-")
      left = int(raw_left)
      right = int(raw_right)
      fresh_pairs.append([left, right])

  # sort the pairs
  sorted_pairs = sorted(fresh_pairs)
  print(f"Sorted pairs {sorted_pairs}")

  old_pairs = sorted_pairs
  new_pairs = combine_groups(sorted_pairs)
  while old_pairs != new_pairs:
    old_pairs = new_pairs
    new_pairs = combine_groups(new_pairs)

  answer = 0
  for pair in new_pairs:
    answer += pair[1] - pair[0] + 1
  print(new_pairs)
  print(answer)


def combine_groups(pairs):
  new_pairs = []
  print(f"Parsing {pairs}")
  for i in range(len(pairs)):
    print(f"  Start of loop {i}, evaluating {pairs[i]}, currently new pairs are {new_pairs}")
    if i == 0:
      new_pairs.append(pairs[i])
      continue

    cur_left, cur_right = pairs[i]
    prev_right = new_pairs[-1][1]

    # overlaps/extends to the right the previous term
    # cur_left can't be less than prev_left due to sorting
    if cur_left <= prev_right:
      if cur_right >= prev_right:
        # extend the previous group
        new_pairs[-1][1] = cur_right
        continue
      else:
        # Value was a subset of the existing range
        continue
    else:
      new_pairs.append(pairs[i])
      continue
  print(f"started with {pairs}, returning {new_pairs}")

  return new_pairs



if __name__ == "__main__":
  main()