# Use sample inputs
# with open("sample.txt", "r") as file:
#     raw_data = file.readlines()

with open("input.txt", "r") as file:
    raw_data = file.readlines()

random_nums = map(lambda str_num: int(str_num), raw_data[0].rstrip().split(','))

# Handle raw data
# For checking rows
total_boards = []
one_board = []
for data in raw_data[2:]:
    if data == '\n':
        total_boards.append(one_board)
        one_board = []
        continue
    row = map(lambda str_num: int(str_num), filter(lambda e: e != '', data.rstrip().split(' ')))
    one_board.append(row)
    if data == raw_data[-1]:
        total_boards.append(one_board)

# For checking columns
board_size = len(total_boards[0])
rotated_boards = []
for board in total_boards:
    rotated_board = [[0] * board_size for r in range(board_size)]
    for i in range(board_size):
        for j in range(board_size):
            rotated_board[j][i] = board[i][j]
    rotated_boards.append(rotated_board)


def check_match(boards1, boards2, num):
    for b in boards1:
        for r in b:
            if num in r:
                r.remove(num)
        if [] in b:
            return b

    for b in boards2:
        for r in b:
            if num in r:
                r.remove(num)
        if [] in b:
            return b


def check_board_after_each_num(boards1, boards2, rand_nums):
    for nmb in rand_nums:
        bingo_board = check_match(boards1, boards2, nmb)
        if bingo_board is not None:
            print("found!")
            return bingo_board, nmb


def sum_up_all_unmarked(bd):
    total = 0
    for r in bd:
        if r is not None:
            for nmb in r:
                total += nmb
    return total


def calculate_score(num, sum_val):
    return num * sum_val


(board_bingoed, the_number) = check_board_after_each_num(total_boards, rotated_boards, random_nums)
print(board_bingoed)
unmarked_sum = sum_up_all_unmarked(board_bingoed)
final_score = calculate_score(the_number, unmarked_sum)
print("Answer for Part 1: " + str(final_score))


