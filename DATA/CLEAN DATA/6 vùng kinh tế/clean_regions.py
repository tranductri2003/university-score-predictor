import pandas as pd

# Đọc file CSV
df = pd.read_csv(r'DATA\RAW DATA\6 vùng kinh tế\regions_data.csv')

# Thực hiện sửa đổi
df['Địa phương'] = df['Địa phương'].str.replace('thành phố ', 'TP. ')
df['Địa phương'] = df['Địa phương'].apply(lambda x: x.split(' và ') if ' và ' in x else [x])

# Tạo DataFrame mới với các dòng được tách ra nếu cần
new_rows = []
for idx, row in df.iterrows():
    if isinstance(row['Địa phương'], list):
        for item in row['Địa phương']:
            new_row = row.copy()
            # Loại bỏ dấu chấm cuối cùng
            item = item.rstrip('.')
            new_row['Địa phương'] = item
            new_rows.append(new_row)
    else:
        new_row = row.copy()
        # Loại bỏ dấu chấm cuối cùng
        new_row['Địa phương'] = new_row['Địa phương'].rstrip('.')
        # Thay thế chuỗi 'Thừa Thiên - Huế' thành 'Thừa Thiên Huế'
        new_row['Địa phương'] = new_row['Địa phương'].replace('Thừa Thiên - Huế', 'Thừa Thiên Huế')
        new_rows.append(new_row)

new_df = pd.DataFrame(new_rows)

# Lưu ra file CSV
new_df.to_csv(r'DATA\CLEAN DATA\6 vùng kinh tế\regions_data.csv', index=False)

print("File CSV đã được lưu thành công.")