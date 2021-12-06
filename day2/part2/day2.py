class Navigation:
    def __init__(self, inputdatafile):
        self.input_file = inputdatafile

    def read_data_file(self):
        with open(self.input_file, 'r') as file:
            data_list = file.read().split('\n')
        return data_list

    def calculate_the_course(self):
        horizontal_position, depth_value, aim_value = 0, 0, 0
        data_list = self.read_data_file()
        for data in data_list:
            data_split = data.split(" ")
            direction = data_split[0]
            value = data_split[1]
            match direction:
                case "up":
                    aim_value -= int(value)
                case "down":
                    aim_value += int(value)
                case "forward":
                    horizontal_position += int(value)
                    depth_value += int(value) * aim_value
        print(horizontal_position * depth_value)
