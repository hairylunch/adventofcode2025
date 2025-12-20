from functools import cache

with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

@cache
# start row is the row past the splitter
def count_paths(start_row, col):
  print(f"Evaluating starting at row {start_row}, column {col}")
  beams = {col}
  paths = 0
  for row, line in enumerate(raw_input_lines[start_row + 1:]):
    print(f"  local row: {row} is {line.strip()}")
    if line[col] == '^':
      next_row = row + start_row + 2
      paths += count_paths(next_row, col - 1) + count_paths(next_row, col + 1)
      break
  if paths == 0:
    return 1

  return paths



start_col = raw_input_lines[0].find("S")
print( count_paths(1, start_col) )


