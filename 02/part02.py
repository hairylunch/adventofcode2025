with open('input.txt', 'r') as f:
  raw_input = f.read().strip()

# raw_input='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

raw_ranges = raw_input.split(',')
print(raw_ranges)
# these will still be strings
ranges = [range.split('-') for range in raw_ranges]

invalid_ids = []
for start_end_pair in ranges:
  for i in range(int(start_end_pair[0]), int(start_end_pair[1]) + 1 ):
    string_i = str(i)
    length = len(string_i)
    for segment_length in range(1, int(length/2) + 1):
      if length % segment_length == 0:
        segments = [string_i[i:i+segment_length] for i in range(0, len(string_i), segment_length)]
        if len(set(segments)) == 1:
          print(string_i,segments)
          invalid_ids.append(i)

print(sum(set(invalid_ids)))

