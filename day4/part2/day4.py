class BingoGame:
    def __init__(self, inputdatafile):
        self.input_file = inputdatafile

    def parse_data_file(self):
        boards = []
        board = []
        with open(self.input_file, 'r') as file:
            data_list = file.read().split('\n')
        played_numbers = data_list[0].split(",")
        for index, data in enumerate(data_list[2:]):
            if data != "":
                digits = data.split(" ")
                for digit in digits:
                    if digit == "":
                        digits.remove(digit)
                board.append(digits)
            if data == "" or index == len(data_list) - 3:
                boards.append(board)
                board = []
        return played_numbers, boards

    def fill_boards(self):
        played_numbers, boards = self.parse_data_file()
        solved_boards = []
        for number in played_numbers:
            for index_boards, board in enumerate(boards):
                if index_boards not in solved_boards:
                    column_counter = [0, 0, 0, 0, 0]
                    for index_board, board_row in enumerate(board):
                        for index_row, board_digit in enumerate(board_row):
                            if board_digit == number:
                                board_row[index_row] = "X"
                        if board_row.count("X") == 5:
                            solved_boards.append(index_boards)
                        else:
                            for dig_index, digit in enumerate(board_row):
                                if digit == "X":
                                    column_counter[dig_index] += 1
                        if column_counter.count(5) == 1:
                            solved_boards.append(index_boards)
                if len(solved_boards) == len(boards):
                    return boards[solved_boards[-1]], number

    def get_result(self):
        sum = 0
        board, number = self.fill_boards()
        for row in board:
            for num in row:
                if num != "X":
                    sum += int(num)
        print("Result: " + str(sum * int(number)))
