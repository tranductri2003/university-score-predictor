import pandas as pd

# Đọc file CSV với mã hóa UTF-8
df = pd.read_csv('DATA\RAW DATA\Dân số và mật độ dân số [2018-2023]\Population_of_provinces.csv', encoding='utf-8', thousands=',')

# Tách dữ liệu thành các cột mới
new_rows = []
for index, row in df.iterrows():
    for year in range(2018, 2023):
        new_row = {}
        new_row['Địa phương'] = row['Địa phương']
        new_row['Năm'] = year
        new_row['Dân số trung bình (Nghìn người)'] = float(row[f'Dân số trung bình (Nghìn người) {year}'].replace('.', '').replace(',', '.'))
        new_row['Mật độ dân số (Người/km2)'] = float(row[f'Mật độ dân số (Người/km2) {year}'].replace('.', '').replace(',', '.'))
        new_rows.append(new_row)

# Tạo DataFrame mới từ các dòng đã sửa đổi
new_df = pd.DataFrame(new_rows)

# Sửa tên 'Thừa Thiên Huế' thành 'Thừa Thiên - Huế'
new_df['Địa phương'] = new_df['Địa phương'].replace('Thừa Thiên Huế', 'Thừa Thiên - Huế')

# Sửa 'TP.' thành 'TP.'
new_df['Địa phương'] = new_df['Địa phương'].str.replace('TP.', 'TP. ')

new_df['Địa phương'] = new_df['Địa phương'].str.replace('Cần Thơ', 'TP. Cần Thơ')

new_df['Địa phương'] = new_df['Địa phương'].str.replace('oà', 'òa')

new_df['Địa phương'] = new_df['Địa phương'].str.replace('oá', 'óa')

# Lưu ra file CSV
new_df.to_csv('DATA\CLEAN DATA\Dân số và mật độ dân số [2018-2023]\clean_population.csv', index=False, encoding='utf-8')

print("File CSV đã được lưu thành công.")