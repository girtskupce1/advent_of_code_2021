class BinaryDiagnostic:
    def __init__(self, inputdatafile):
        self.input_file = inputdatafile
        self.data_list = self.read_data_file()
        self.dict_length = 0

    def read_data_file(self):
        with open(self.input_file, 'r') as file:
            data_list = file.read().split('\n')
        return data_list

    def populate_dictionary(self, data_list):
        most_common_number_per_column = {}
        longest_string = max(data_list, key=len)
        for int in range(len(longest_string)):
            most_common_number_per_column[str(int + 1)] = 0
        return most_common_number_per_column

    def calculate_most_present_number(self, data_list):
        number_dict = self.populate_dictionary(data_list)
        for row in data_list:
            for index, element in enumerate(list(row)):
                if int(element) == 1:
                    number_dict[str(int(index) + 1)] += 1
                else:
                    number_dict[str(int(index) + 1)] -= 1
        self.dict_length = len(number_dict)
        return number_dict

    def get_rating_value(self, minor_value=False):
        temp_result = []
        actual_result = []
        iteration = 0
        self.calculate_most_present_number(self.data_list)
        while iteration < self.dict_length:
            calculated_values_dict = self.calculate_most_present_number(
                self.data_list) if not actual_result else self.calculate_most_present_number(actual_result)
            data_set = self.data_list if not actual_result else actual_result
            if calculated_values_dict[str(iteration + 1)] >= 0:
                for data in data_set:
                    for index, elem in enumerate(data):
                        if int(index) == iteration and (
                                int(elem) == 1 and not minor_value or int(elem) == 0 and minor_value):
                            temp_result.append(data)
            else:
                for data in data_set:
                    for index, elem in enumerate(data):
                        if int(index) == iteration and (
                                int(elem) == 0 and not minor_value or int(elem) == 1 and minor_value):
                            temp_result.append(data)
            actual_result = temp_result
            if len(actual_result) == 1:
                break
            temp_result = []
            iteration += 1
        return int(actual_result[0], 2)

    def calculate_life_support_rating(self):
        oxygen_generator_rating = self.get_rating_value()
        co2_scrubber_rating = self.get_rating_value(True)
        print(oxygen_generator_rating * co2_scrubber_rating)
        # 4125600
