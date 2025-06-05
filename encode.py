import csv

def encode(board):
    sum_ = 0
    count_1 = 0
    count_2 = 0
    for row in range(6):
        for col in range(7):
            if board[row,col] == 0:
                continue
            elif board[row,col] == 1:
                sum_ += (row*7+col) * 42 ** (count_1)
                count_1 += 1
            elif board[row,col] == 2:
                sum_ += (row*7+col) * 42 ** (count_2+4)
                count_2 += 1
    return sum_

with open('connect-4.data', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate through each row in the file
    features = []
    label = []
    for row in csv_reader:
        # The last element is the label
        features.append(row[:-1])  # All except the last element
        label.append(row[-1])  # The last element (the label)

# This encodes the connect 4 dataset into a number and puts it either into the win or lose list
win_ = []
lose_ = []
for i in range(len(features)):
    sum_ = 0
    count_1 = 0
    count_2 = 0
    for j in range(42):
        row = 5 - j % 6
        col = j // 6
        if features[i][j] == 'x':
            sum_ += (row*7+col) * 42 ** (count_1)
            count_1 += 1
        elif features[i][j] == 'o':
            sum_ += (row*7+col) * 42 ** (count_2+4)
            count_2 += 1
    
    if label[i] == "win":
        win_.append(sum_)
    elif label[i] == "loss":
        lose_.append(sum_)

print("Number of winning positions: ", len(win_))
print("Number of losing positions: ", len(lose_))

with open('win_.txt', 'w+') as f:
    for item in win_:
        f.write(f"{item},")

with open('lose_.txt', 'w+') as f:
    for item in lose_:
        f.write(f"{item},")