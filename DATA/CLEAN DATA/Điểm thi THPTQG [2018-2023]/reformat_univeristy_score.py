import os
import pandas as pd
import difflib

PROVINCE_NAMES = [
    'Hà Giang', 'Cao Bằng', 'Lạng Sơn', 'Bắc Giang', 'Phú Thọ', 'Thái Nguyên', 'Bắc Kạn', 'Tuyên Quang', 
    'Lào Cai', 'Yên Bái', 'Lai Châu', 'Sơn La', 'Điện Biên', 'Hòa Bình', 'Hà Nội', 'Hải Phòng', 'Hải Dương', 
    'Hưng Yên', 'Vĩnh Phúc', 'Bắc Ninh', 'Thái Bình', 'Nam Định', 'Hà Nam', 'Ninh Bình', 'Quảng Ninh', 
    'Thanh Hóa', 'Nghệ An', 'Hà Tĩnh', 'Quảng Bình', 'Quảng Trị', 'Thừa Thiên - Huế', 'Đà Nẵng', 'Quảng Nam', 
    'Quảng Ngãi', 'Bình Định', 'Phú Yên', 'Khánh Hòa', 'Ninh Thuận', 'Bình Thuận', 'Kon Tum', 'Gia Lai', 
    'Đắk Lắk', 'Đắk Nông', 'Lâm Đồng', 'TP. Hồ Chí Minh', 'Đồng Nai', 'Bà Rịa - Vũng Tàu', 'Bình Dương', 
    'Bình Phước', 'Tây Ninh', 'TP. Cần Thơ', 'Long An', 'Tiền Giang', 'Bến Tre', 'Trà Vinh', 'Vĩnh Long', 
    'An Giang', 'Đồng Tháp', 'Kiên Giang', 'Hậu Giang', 'Sóc Trăng', 'Bạc Liêu', 'Cà Mau'
]

def normalize_province_name(name):
    if name == 'Thành phố Hà Nội':
        return 'Hà Nội'
    elif name == 'Thành phố Đà Nẵng':
        return 'Đà Nẵng'
    else:
        matches = difflib.get_close_matches(name, PROVINCE_NAMES)
        if matches:
            return matches[0]
        else:
            return name


def add_average_column(file_path, destination_folder, destination_csv):
    # Đọc file CSV
    df = pd.read_csv(file_path)

    # Thêm cột TBC (Trung bình cộng)
    df['TBC'] = (df['Điểm Toán'] + df['Điểm Văn'] + df['Điểm Anh']) / 3

    # Lấy thông tin năm và địa phương từ tên file
    file_name = os.path.basename(file_path)
    name_without_extension = os.path.splitext(file_name)[0]
    year, province = name_without_extension.split('_')[:2]

    # Chuẩn hóa tên thành phố
    province = normalize_province_name(province)

    # Tạo tên file mới
    new_file_name = name_without_extension + '_reformat.csv'
    new_file_path = os.path.join(destination_folder, new_file_name)

    # Lưu ra file CSV mới
    df.to_csv(new_file_path, index=False)
    
    return df['TBC'].mean(), year, province

# Thư mục chứa các file CSV
source_folder = r'DATA\RAW DATA\Điểm thi THPTQG [2018-2023]\CSV_Files'
# Thư mục đích cho các file CSV mới
destination_folder = r'DATA\CLEAN DATA\Điểm thi THPTQG [2018-2023]\Reformat_CSV_Files'
# Tạo file csv mới để thống kê TBC cho từng tỉnh, từng năm
destination_csv = r'DATA\CLEAN DATA\Điểm thi THPTQG [2018-2023]\university_scores_reformat.csv'

# Tạo thư mục đích nếu nó chưa tồn tại
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Tạo danh sách để tích lũy dữ liệu
data = []

# Lặp qua các file trong thư mục nguồn
for file_name in os.listdir(source_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(source_folder, file_name)
        score, year, province = add_average_column(file_path, destination_folder, destination_csv)
        # Thêm dữ liệu vào danh sách
        data.append({'Địa phương': province, 'Năm': year, 'Giá trị': score})

# Tạo DataFrame từ danh sách
df_result = pd.DataFrame(data)

# Lưu DataFrame vào file CSV
df_result.to_csv(destination_csv, index=False)

print("Đã xử lý xong tất cả các file CSV.")
