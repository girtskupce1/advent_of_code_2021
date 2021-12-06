class BinaryDiagnostic:
    def __init__(self, inputdatafile):
        self.input_file = inputdatafile

    def read_data_file(self):
        with open(self.input_file, 'r') as file:
            data_list = file.read().split('\n')
        return data_list

    def populate_dictionary(self, data_list):
        most_common_number_per_column = {}
        longest_string = max(data_list, key=len)
        for int in range(len(longest_string)):
            most_common_number_per_column[str(int+1)] = 0
        return most_common_number_per_column

    def calculate_most_and_least_present_number(self):
        data_list = self.read_data_file()
        number_dict = self.populate_dictionary(data_list)
        for row in data_list:
            for index, element in enumerate(list(row)):
                if int(element) == 1:
                    number_dict[str(int(index) + 1)] += 1
                else:
                    number_dict[str(int(index) + 1)] -= 1
        print(number_dict)
        return number_dict

    def get_gamma_and_epsilon_rates(self):
        gamma_rate, epsilon_rate = "", ""
        calculated_values_dict = self.calculate_most_and_least_present_number()
        for index,_ in enumerate(calculated_values_dict):
            if calculated_values_dict[str(index+1)] > 0:
                gamma_rate += "1"
                epsilon_rate += "0"
            else:
                gamma_rate += "0"
                epsilon_rate += "1"
        gamma_rate_decimal = int(gamma_rate, 2)
        epsilon_rate_decimal = int(epsilon_rate, 2)
        print(gamma_rate_decimal * epsilon_rate_decimal)