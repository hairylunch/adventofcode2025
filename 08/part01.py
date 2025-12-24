import itertools
import pprint

from collections import defaultdict

input_file = 'input.txt'
connections = 1000
# input_file = 'input-test.txt'
# connections = 10

with open(input_file, 'r') as f:
  raw_input_lines = f.readlines()

points = [list(map(int, line.strip().split(','))) for line in raw_input_lines]

squared_distance_to_points = defaultdict(list)
for point_pair in itertools.combinations(points, 2):
  squared_distance = 0
  for i in range(3):
    squared_distance += (point_pair[0][i] - point_pair[1][i]) ** 2
  # Add pair with coordinates as strings
  squared_distance_to_points[squared_distance].append({str(point_pair[0]), str(point_pair[1])})

sorted_squared_distances = sorted(squared_distance_to_points)

# make the connections / pairs; could be longer than `connections`` in theory if there were pairs with same distances
pairs = []
for i in sorted_squared_distances[:connections]:
  for pair in squared_distance_to_points[i]:
    pairs.append(set(pair))

# find out which points are connected, constructing lists of the sets points that make up a circuit
new_circuits = pairs
old_circuits = []

while old_circuits != new_circuits:
  old_circuits = new_circuits
  new_circuits = []
  for i, circuit in enumerate(old_circuits[:-1]):
    overlap_found = False
    for j, later_circuit in enumerate(old_circuits[i+1:]):
      if circuit.intersection(later_circuit):
        overlap_found = True
        # add the union and all the others
        new_circuits.append(circuit.union(later_circuit))
        for k, c in enumerate(old_circuits):
          if k not in [i, j+i+1]:
            new_circuits.append(c)
        break
    if overlap_found:
      break
  if new_circuits == []:
    break
print(pprint.pformat(old_circuits), pprint.pformat(new_circuits))

sorted_lengths = sorted([len(circuit) for circuit in old_circuits], reverse=True)
print(sorted_lengths)
answer = 1
for i in [0,1,2]:
  answer *= sorted_lengths[i]

print(answer)


# 2873 too low
# 3808 too low