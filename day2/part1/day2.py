class Navigation:
    def __init__(self, inputdatafile):
        self.input_file = inputdatafile

    def read_data_file(self):
        data_dict = {"forward": 0, "up": 0, "down": 0}
        with open(self.input_file, 'r') as file:
            data_list = file.read().split('\n')
        for data in data_list:
            data_split = data.split(" ")
            data_dict[data_split[0]] += int(data_split[1])
        result = data_dict["forward"] * (data_dict["down"] - data_dict["up"])
        print(data_dict)
        print("Final result: " + str(result))

