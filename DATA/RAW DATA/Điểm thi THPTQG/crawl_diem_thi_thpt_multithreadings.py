import requests
from bs4 import BeautifulSoup
import os
import csv
from concurrent.futures import ThreadPoolExecutor

ID_TO_PROVINCE_DICTIONARY = {
    '01': 'Thành phố Hà Nội',
    '02': 'Thành phố Hồ Chí Minh',
    '03': 'Thành phố Hải Phòng',
    '04': 'Thành phố Đà Nẵng',
    '05': 'Tỉnh Hà Giang',
    '06': 'Tỉnh Cao Bằng',
    '07': 'Tỉnh Lai Châu',
    '08': 'Tỉnh Lào Cai',
    '09': 'Tỉnh Tuyên Quang',
    '10': 'Lạng Sơn',
    '11': 'Tỉnh Bắc Kạn',
    '12': 'Tỉnh Thái Nguyên',
    '13': 'Tỉnh Yên Bái',
    '14': 'Tỉnh Sơn La',
    '15': 'Tỉnh Phú Thọ',
    '16': 'Tỉnh Vĩnh Phúc',
    '17': 'Tỉnh Quảng Ninh',
    '18': 'Tỉnh Bắc Giang',
    '19': 'Tỉnh Bắc Ninh',
    '21': 'Tỉnh Hải Dương',
    '22': 'Tỉnh Hưng Yên',
    '23': 'Tỉnh Hòa Bình',
    '24': 'Tỉnh Hà Nam',
    '25': 'Tỉnh Nam Định',
    '26': 'Tỉnh Thái Bình',
    '27': 'Tỉnh Ninh Bình',
    '28': 'Tỉnh Thanh Hóa',
    '29': 'Tỉnh Nghệ An',
    '30': 'Tỉnh Hà Tĩnh',
    '31': 'Tỉnh Quảng Bình',
    '32': 'Tỉnh Quảng Trị',
    '33': 'Tỉnh Thừa Thiên - Huế',
    '34': 'Tỉnh Quảng Nam',
    '35': 'Tỉnh Quảng Ngãi',
    '36': 'Tỉnh Kon Tum',
    '37': 'Tỉnh Bình Định',
    '38': 'Tỉnh Gia Lai',
    '39': 'Tỉnh Phú Yên',
    '40': 'Tỉnh Đắk Lắk',
    '41': 'Tỉnh Khánh Hòa',
    '42': 'Tỉnh Lâm Đồng',
    '43': 'Tỉnh Bình Phước',
    '44': 'Tỉnh Bình Dương',
    '45': 'Tỉnh Ninh Thuận',
    '46': 'Tỉnh Tây Ninh',
    '47': 'Tỉnh Bình Thuận',
    '48': 'Tỉnh Đồng Nai',
    '49': 'Tỉnh Long An',
    '50': 'Tỉnh Đồng Tháp',
    '51': 'Tỉnh An Giang',
    '52': 'Tỉnh Bà Rịa - Vũng Tàu',
    '53': 'Tỉnh Tiền Giang',
    '54': 'Tỉnh Kiên Giang',
    '55': 'Thành phố Cần Thơ',
    '56': 'Tỉnh Bến Tre',
    '57': 'Tỉnh Vĩnh Long',
    '58': 'Tỉnh Trà Vinh',
    '59': 'Tỉnh Sóc Trăng',
    '60': 'Tỉnh Bạc Liêu',
    '61': 'Tỉnh Cà Mau',
    '62': 'Tỉnh Điện Biên',
    '63': 'Tỉnh Đắk Nông',
    '64': 'Tỉnh Hậu Giang'
}

PROVINCE_TO_ID_DICTIONARY = {province_name: province_id for province_id, province_name in ID_TO_PROVINCE_DICTIONARY.items()}

PROVINCE_LIST = list(ID_TO_PROVINCE_DICTIONARY.values())
YEARS = [2018, 2019, 2020, 2021, 2022, 2023]
CRAWL_FIELDS = ["Toán", "Ngữ văn", "Ngoại ngữ"]

CSV_PATH = r"D:\Code\BachKhoa\Khoa Hoc Du Lieu\university-score-predictor\DATA\RAW DATA\Điểm thi THPTQG\CSV_Files"

def process_province(year_province):
    year, province = year_province
    csv_filename = f"{year}_{province}.csv"
    csv_filepath = os.path.join(CSV_PATH, csv_filename)
    print(f"File CSV được lưu tại: {os.path.abspath(csv_filepath)}")

    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['SBD', 'Điểm Toán', 'Điểm Văn', 'Điểm Anh', 'Điểm Trung bình'])
        student_count = 0
        for student_id in range(1, 10000):
            identification_number = PROVINCE_TO_ID_DICTIONARY[province] + '0' * (6 - len(str(student_id))) + str(student_id)
            url = f"https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={identification_number}&nam={year}"
            response = requests.get(url)
            data = response.json()

            if "result" in data and len(data["result"]) > 0:
                result = data["result"][0]
                diem_toan = float(result.get("Toan", 0)) if result.get("Toan", "") != "" else 0
                diem_ngu_van = float(result.get("NguVan", 0)) if result.get("NguVan", "") != "" else 0
                diem_ngoai_ngu = float(result.get("NgoaiNgu", 0)) if result.get("NgoaiNgu", "") != "" else 0
                diem_trung_binh = (diem_toan + diem_ngu_van + diem_ngoai_ngu) / 3
                sbd = result.get("Code", "Không có thông tin")
                writer.writerow([sbd, diem_toan, diem_ngu_van, diem_ngoai_ngu, diem_trung_binh])
                print(f"SBD: {sbd} Điểm toán: {diem_toan} Điểm văn: {diem_ngu_van} Điểm ngoại ngữ: {diem_ngoai_ngu}")
                student_count += 1
                if student_count == 1000:
                    break

# Tạo thư mục CSV nếu chưa tồn tại
if not os.path.exists(CSV_PATH):
    os.makedirs(CSV_PATH)

# Sử dụng ThreadPoolExecutor để chạy đa luồng
with ThreadPoolExecutor() as executor:
    executor.map(process_province, [(year, province) for year in YEARS for province in PROVINCE_LIST])

print("Đã tạo các tệp CSV thành công!")
