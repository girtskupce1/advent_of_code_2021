from datetime import datetime

class DepthReadings:
    def __init__(self, inputdatafile):
        self.input_file = inputdatafile

    def read_data_file(self):
        int_data_list = []
        with open(self.input_file, 'r') as file:
            data_list = file.read().split('\n')
        for row in data_list:
            int_data_list.append(int(row))
        return int_data_list

    def examine_depth_readings(self):
        data_list = self.read_data_file()
        counter = 0
        reading = data_list[0]
        result_list = [str(reading) + " N/A - no previous measurement"]
        for input in data_list[1:]:
            if input > reading:
                counter += 1
                result_list.append(str(input) + " (increased)")
            else:
                result_list.append(str(input) + " (decreased)")
            reading = input
        return counter, result_list

    def write_file(self):
        date = datetime.now()
        result_file_name = "result_file_" + date.strftime("%m_%d_%Y_%H_%M_%S") + ".txt"
        counter, result_list = self.examine_depth_readings()
        with open(result_file_name, 'w') as output_file:
            output_file.write("Counter: " + str(counter) + "\nResults:\n")
            for el in result_list:
                output_file.write(str(el) + "\n")