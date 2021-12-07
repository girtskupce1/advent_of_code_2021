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
        for number in played_numbers:
            for index_boards, board in enumerate(boards):
                column_counter = [0, 0, 0, 0, 0]
                for board_row in board:
                    for index_bord_digit, board_digit in enumerate(board_row):
                        if board_digit == number:
                            board_row[index_bord_digit] = "X"
                    if board_row.count("X") == 5:
                        return number, board
                    else:
                        for dig_index, digit in enumerate(board_row):
                            if digit == "X":
                                column_counter[dig_index] += 1
                    if column_counter.count(5) == 1:
                        return number, board

    def get_result(self):
        sum = 0
        number, board = self.fill_boards()
        for row in board:
            for num in row:
                if num != "X":
                    sum += int(num)
        print("Result: " + str(sum * int(number)))
