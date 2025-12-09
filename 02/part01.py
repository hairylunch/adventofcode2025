with open('input.txt', 'r') as f:
  raw_input = f.read().strip()

raw_input='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

raw_ranges = raw_input.split(',')
print(raw_ranges)
# these will still be strings
ranges = [range.split('-') for range in raw_ranges]

invalid_sum = 0
for start_end_pair in ranges:
  for i in range(int(start_end_pair[0]), int(start_end_pair[1]) + 1 ):
    string_i = str(i)
    length = len(string_i)
    if length % 2 == 0:
      midpoint = int(length/2)
      if string_i[:midpoint] == string_i[midpoint:]:
        invalid_sum += i
        print(invalid_sum, string_i)
