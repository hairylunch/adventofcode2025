

def main():

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

  removed_rolls = 0
  removable_rolls = find_removable_rolls(grid)
  while removable_rolls:
    print(f"Removing {len(removable_rolls)} rolls at {removable_rolls}")
    # remove the rolls
    removed_rolls += len(removable_rolls)
    for i in removable_rolls:
      row, col = i[0], i[1]
      row_to_edit = grid[row]
      grid[row] = row_to_edit[:col] + 'x' + row_to_edit[col + 1:]
    removable_rolls = find_removable_rolls(grid)
  print(removed_rolls)



def find_removable_rolls(grid):
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
  return accessible_rolls



if __name__ == "__main__":
  main()