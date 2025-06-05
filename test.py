import numpy as np

def max_connected(piece, state):
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

    max_score = 0

    for row in range(len(state)):
        for col in range(len(state[0])):
            if state[row][col] == piece:
                for dr, dc in directions:
                    count = 1
                    potential_count = 1
                    # Check in the positive direction
                    r, c = row, col
                    while True:
                        r += dr
                        c += dc
                        if (r < 0 or c < 0 or r >= len(state) or c >= len(state[0]) 
                        or state[r][c] == 3 - piece): # oob or opp
                            #print(r, c)
                            #print("xx")
                            count = 0
                            #print("count 0", row, col, count)
                            max_score = max(max_score, count)
                            break
                        elif state[r][c] == piece: # player
                            #print(r, c)
                            #print("pp")
                            potential_count += 1
                            count += 1
                            if count == 4:
                                return 4
                            elif potential_count == 4:
                                max_score = max(max_score, count)
                                #print("count ?", row, col, count)
                                break
                            else:
                                continue
                        else: # 0
                            #print(r, c)
                            #print("00")
                            potential_count += 1
                            #print("potential_count:", potential_count)
                            if potential_count == 4:
                                max_score = max(max_score, count)
                                #print("count ?", row, col, count)
                                break
                            else:
                                continue

    return max_score

# Example board
board = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [1, 2, 2, 2, 1, 0, 0],
])

piece = 1
print("Max 1:", max_connected(1, board))
print("Max 2:", max_connected(2, board))