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

    def calculate_readings(self):
        data_list = self.read_data_file()
        calculated_reading_list = []
        for index, data in enumerate(data_list):
            try:
                calculated_reading_list.append(data + data_list[index+1] + data_list[index+2])
            except IndexError:
                break
        return calculated_reading_list

    def examine_depth_readings(self):
        data_list = self.calculate_readings()
        counter = 0
        calculated_data = data_list[0]
        result_list = [str(calculated_data) + " N/A - no previous measurement"]
        for reading in data_list[1:]:
            if reading > calculated_data:
                counter += 1
                result_list.append(str(reading) + " (increased)")
            elif reading == calculated_data:
                result_list.append(str(reading) + " (no change)")
            else:
                result_list.append(str(reading) + " (decreased)")
            calculated_data = reading
        return counter, result_list

    def write_results_in_file(self):
        date = datetime.now()
        result_file_name = "result_file_" + date.strftime("%m_%d_%Y_%H_%M_%S") + ".txt"
        counter, result_list = self.examine_depth_readings()
        with open(result_file_name, 'w') as output_file:
            output_file.write("Counter: " + str(counter) + "\nResults:\n")
            for el in result_list:
                output_file.write(str(el) + "\n")