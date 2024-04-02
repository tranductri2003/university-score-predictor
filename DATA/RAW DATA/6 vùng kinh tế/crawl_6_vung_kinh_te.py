import requests
from bs4 import BeautifulSoup
import csv

# URL của bài viết chứa thông tin về 6 vùng kinh tế
url = "https://nangluongsachvietnam.vn/d6/vi-VN/news/Chia-ca-nuoc-thanh-6-vung-kinh-te-xa-hoi-0-185-17497"

# Gửi yêu cầu GET đến URL
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (status code 200)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích nội dung HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Tạo một từ điển để lưu trữ thông tin về các vùng kinh tế-xã hội và các tỉnh/thành phố trong mỗi vùng
    regions_data = {}
    
    # Tìm tất cả các thẻ <p> trong bài viết
    paragraphs = soup.find_all("p")
    
    # Duyệt qua từng đoạn văn trong bài viết để tìm thông tin về các tỉnh thành
    for paragraph in paragraphs:
        # Lấy nội dung của đoạn văn
        text = paragraph.get_text().strip()
        # Kiểm tra nếu đoạn văn chứa thông tin về các tỉnh thành và lưu vào từ điển regions_data
        if "Vùng trung du và miền núi phía Bắc" in text:
            northern_mountainous_provinces = text.split(": ")[1].split(", ")
            regions_data["Vùng trung du và miền núi phía Bắc"] = northern_mountainous_provinces
        elif "Vùng đồng bằng sông Hồng" in text:
            red_river_delta_provinces = text.split(": ")[1].split(", ")
            regions_data["Vùng đồng bằng sông Hồng"] = red_river_delta_provinces
        elif "Vùng Bắc Trung Bộ và duyên hải miền Trung" in text:
            north_central_provinces = text.split(": ")[1].split(", ")
            regions_data["Vùng Bắc Trung Bộ và duyên hải miền Trung"] = north_central_provinces
        elif "Vùng Tây Nguyên" in text:
            central_highlands_provinces = text.split(": ")[1].split(", ")
            regions_data["Vùng Tây Nguyên"] = central_highlands_provinces
        elif "Vùng Đông Nam Bộ" in text:
            southeast_provinces = text.split(": ")[1].split(", ")
            regions_data["Vùng Đông Nam Bộ"] = southeast_provinces
        elif "Vùng đồng bằng sông Cửu Long" in text:
            mekong_delta_provinces = text.split(": ")[1].split(", ")
            regions_data["Vùng đồng bằng sông Cửu Long"] = mekong_delta_provinces
    
    # Ghi thông tin vào tệp CSV
    with open("regions_data.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Viết tiêu đề cho các cột
        writer.writerow(["Vùng kinh tế - Xã hội", "Địa phương"])
        # Duyệt qua từng cặp key-value trong từ điển và viết vào file CSV
        for region, provinces in regions_data.items():
            for province in provinces:
                writer.writerow([region, province])
else:
    print("Yêu cầu không thành công, mã trạng thái:", response.status_code)
