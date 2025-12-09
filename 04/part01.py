with open('input.txt', 'r') as f:
  raw_input_lines = f.readlines()

grid = [line.strip() for line in raw_input_lines]

# grid = [
# '..@@.@@@@.',
# '@@@.@.@.@@',
# '@@@@@.@.@@',
# '@.@@@@..@.',
# '@@.@@@@.@@',
# '.@@@@@@@.@',
# '.@.@.@.@@@',
# '@.@@@.@@@@',
# '.@@@@@@@@.',
# '@.@.@@@.@.',
# ]

min_row = 0
max_row = len(grid) - 1
min_col = 0
max_col = len(grid[0]) - 1
accessible_rolls = []
for r, row in enumerate(grid):
  print(r, row)
  for c, col in enumerate(row):
    if col == '@':
      print(f"Evaluating roll at {r}, {c}...")
      neighbors = 0
      for row_offset in (-1, 0, 1):
        for col_offset in (-1, 0, 1):
          test_row = r + row_offset
          test_col = c + col_offset
          print(f"  {test_row}, {test_col} being checked")
          if (not (test_row == r and test_col == c)
              and min_col <= test_col <= max_col
              and min_row <= test_row <= max_row):
            if grid[test_row][test_col] == '@':
              print(f"    Found adjacent role at {test_row}, {test_col}")
              neighbors += 1
          else:
            # print(min_col <= test_col <= max_col, min_col, test_col, max_col)
            # print(min_row <= test_row <= max_row, min_row, test_row, max_row)
            print(f"  {test_row}, {test_col} is not a valid test location")
      if neighbors < 4:
        accessible_rolls.append([r, c])
        print(f"Roll at {r}, {c} is accessible")

print(accessible_rolls)
print(len(accessible_rolls))


