class FactorHandler:
    def __init__(self):
        self.factors = []

    def add_factor(self, time_format, time, value):
        standard_time = self.convert_to_standard_format(time_format, time)
        self.factors.append({"time": standard_time, "value": value})

    def remove_all_factors(self, time_format, time):
        standard_time = self.convert_to_standard_format(time_format, time)
        self.factors = [factor for factor in self.factors if factor["time"] != standard_time]

    def get_sum(self, time_format, start_time, finish_time):
        start_time = self.convert_to_standard_format(time_format, start_time)
        finish_time = self.convert_to_standard_format(time_format, finish_time)

        total_sum = sum(factor["value"] for factor in self.factors
                        if start_time <= factor["time"] <= finish_time)

        return total_sum

    def convert_to_standard_format(self, time_format, time):
        if time_format == "dd/mm/yyyy":
            parts = time.split("/")
            return f"{parts[2]}/{parts[1]}/{parts[0]}"
        elif time_format == "yyyy/mm/dd":
            return time
        elif time_format == "yyyy/dd/mm":
            parts = time.split("/")
            return f"{parts[0]}/{parts[2]}/{parts[1]}"

fh = FactorHandler()
fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)

result = fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10")
print(result)

