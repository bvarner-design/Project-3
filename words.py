def num_letters(num_rows,num_columns):
    return 2 * num_rows + 2* num_columns - 4

assert num_letters(3, 4) == 10  #3 is the num_rows and 4 is the num_columns

print("Checking assertions.")

import numpy as np

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

words = [] 

rows, columns = data.shape
for r in range(rows):
    for c in range(columns):
        if data[r,c] != '':
            words.append(data[r,c])

print(words)
#print("Rows:", rows)
#print("Columns:", columns)
#print("Letters collected:", len(words))
#print("Expected:", num_letters(rows, columns))
assert len(words) == num_letters(rows, columns)


word = []
# top row 
for c in range(columns - 1):
    words.append(data[0,c]+ data[0, c + 1])
# right side
for r in range(rows - 1):
    words.append(data[r, columns - 1] + data[r +1, columns - 1])

# Bottom row (right to left)
for c in range(columns - 1, 0, -1):
    words.append(data[rows - 1, c] + data[rows - 1, c - 1])

# Left side (bottom to top)
for r in range(rows - 1, 0, -1):
    words.append(data[r, 0] + data[r - 1, 0])

print (words)
  
