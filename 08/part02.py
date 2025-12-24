import itertools
import ast
import pprint

from collections import defaultdict

input_file = 'input.txt'
# input_file = 'input-test.txt'

with open(input_file, 'r') as f:
  raw_input_lines = f.readlines()

points = [list(map(int, line.strip().split(','))) for line in raw_input_lines]

squared_distance_to_points = defaultdict(list)
# build the pairs as well as a set of all the junction boxes
all_boxes = set()
for point_pair in itertools.combinations(points, 2):
  squared_distance = 0
  for i in range(3):
    squared_distance += (point_pair[0][i] - point_pair[1][i]) ** 2
  # Add pair with coordinates as strings
  squared_distance_to_points[squared_distance].append({str(point_pair[0]), str(point_pair[1])})
  all_boxes.add(str(point_pair[0]))
  all_boxes.add(str(point_pair[1]))

sorted_squared_distances = sorted(squared_distance_to_points)

pairs = []
for i in sorted_squared_distances:
  for pair in squared_distance_to_points[i]:
    pairs.append(set(pair))

# find out which points are connected, constructing lists of the sets points that make up a circuit
new_circuits = pairs
old_circuits = []

while old_circuits != new_circuits:
  # print(f"Processing, starting length {len(new_circuits)}")
  # print(f"{pprint.pformat(old_circuits)}, {pprint.pformat(new_circuits)}")
  old_circuits = new_circuits
  new_circuits = []
  overlap_found = False
  circuit = old_circuits[0]
  for i, later_circuit in enumerate(old_circuits[1:]):
    if circuit.intersection(later_circuit):
      overlap_found = True

      combined_circuit = circuit.union(later_circuit)
      # short circuit if we did the last merge/found the answer
      if combined_circuit == all_boxes:
        answer = 1
        for i in later_circuit:
          print(i)
          answer *= ast.literal_eval(i)[0]
        # print(later_circuit)
        print(answer)
        exit()

      # add the union and all the others
      # print(f"Adding {combined_circuit} - union of {circuit} and {later_circuit}")
      new_circuits.append(combined_circuit)
      # print(f"After adding: {new_circuits}")
      for j, c in enumerate(old_circuits):
        if j not in [0, i+1]:
          new_circuits.append(c)
      # print(f"After adding the rest: {new_circuits}")
      break
  # no combinations found, pop the first element
  if not overlap_found:
    new_circuits = new_circuits[1:]


