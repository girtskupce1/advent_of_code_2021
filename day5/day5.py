class HydrothermalVenture:
    def __init__(self, input_data_file):
        self.input_file = input_data_file

    def parse_file(self):
        parsed_data_file = []
        with open(self.input_file, 'r') as file:
            data_list = file.read().split('\n')
        for coordinates in data_list:
            parsed_data_file.append(coordinates.split(" -> "))

        # print(parsed_data_file)
        dict = {}
        for parsed_data in parsed_data_file:
            x1 = int(parsed_data[0].split(",")[0])
            x2 = int(parsed_data[1].split(",")[0])
            y1 = int(parsed_data[0].split(",")[1])
            y2 = int(parsed_data[1].split(",")[1])

            dict[str(x1) + "," + str(y1)] = 0
            dict[str(x2) + "," + str(y2)] = 0

            x_delta = x1 - x2
            y_delta = y1 - y2

            # if x_delta:
            for x in range(abs(x_delta)):
                # for y in range(abs(y_delta)):
                if x_delta > 0:
                    if str(x) + "," + str(y1) in dict.keys():
                        dict[str(x) + "," + str(y1)] += 1
                    else:
                        dict[str(x) + "," + str(y1)] = 0

                else:
                    if dict[str(x) + "," + str(y1)]:
                        dict[str(x) + "," + str(y1)] += 1
                    else:
                        dict[str(x) + "," + str(y1)] = 0


            print(dict)

            # print(x_delta, y_delta)