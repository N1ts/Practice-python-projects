def get_temperature():
    with open("temperatue.txt", "r") as file:
        data = file.readlines()
        data_new = data[1:]
        values = [float(i) for i in data_new]
        print(values)
        temp_average = sum(values)/len(data_new)
    return temp_average

average = get_temperature()
print(average)