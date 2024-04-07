import csv

# Đọc dữ liệu từ file test.csv
with open('DATA\RAW DATA\Chỉ số phát triển con người [2018-2020]\Thống kê chỉ số giai đoạn 2018 - 2020 - 1. Chỉ số phát triển con người của cả nước và các địa phương giai đoạn 2018 - 2020.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Tạo danh sách địa phương và loại bỏ hàng đầu tiên (tiêu đề)
locations = ['TP. Cần Thơ' if location == 'Cần Thơ' else 'Hòa Bình' if location == 'Hoà Bình' else location for location in [row[0] for row in data[1:]]]
# Tạo danh sách giá trị của mỗi năm
values_2018 = [row[1] for row in data[1:]]
values_2019 = [row[2] for row in data[1:]]
values_2020 = [row[3] for row in data[1:]]

# Tạo danh sách tuples (địa phương, năm, giá trị) từ dữ liệu đã tách
reformatted_data = []
for location, value_2018, value_2019, value_2020 in zip(locations, values_2018, values_2019, values_2020):
    reformatted_data.append((location, '2018', value_2018))
    reformatted_data.append((location, '2019', value_2019))
    reformatted_data.append((location, '2020', value_2020))

# Ghi dữ liệu đã được chuyển đổi vào file reformat.csv
with open('DATA\CLEAN DATA\Chỉ số phát triển con người [2018-2020]\Chỉ số phát triển con người [2018-2020].csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Địa phương', 'Năm', 'Giá trị'])  # Viết tiêu đề cột
    writer.writerows(reformatted_data)
