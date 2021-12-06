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


# different than part 1
def check_match(boards1, boards2, num):
    found_a_bingo = False
    b_to_return = None
    index_to_return = None

    for index, b in enumerate(boards1):
        print(index)
        print("board 1")
        print(num)
        for r in b:
            if num in r:
                r.remove(num)

    for index, b in enumerate(boards2):
        print(boards2)
        print(index)
        print("board 2")
        print(num)
        for r in b:
            if num in r:
                r.remove(num)

    for index, b in enumerate(boards1):
        if [] in b:
            b_to_return = b
            index_to_return = index

    for index, b in enumerate(boards2):
        if [] in b:
            b_to_return = b
            index_to_return = index

    if b_to_return is not None and index_to_return is not None:
        return b_to_return, index_to_return
    else:
        return None


# different than part 1
def check_board_after_each_num(boards1, boards2, rand_nums):
    for nmb in rand_nums:
        if check_match(boards1, boards2, nmb) is None:
            print("no bingo and return this time")
            continue
        else:
            (bingo_board, index) = check_match(boards1, boards2, nmb)
            print("!!!!!!!!!!!!!!!found a bingo in a board, need to delete that board")
            if len(boards1) != 1 and len(boards2) != 1:
                print("deleted that bingo board, but continue..")
                boards1.remove(boards1[index])
                boards2.remove(boards2[index])
            else:
                print("************found the last board to win!!")
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
print("Answer for Part 2: " + str(final_score))


