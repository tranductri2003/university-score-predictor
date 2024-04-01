import requests
from bs4 import BeautifulSoup

# URL của trang web
url = "https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/47000001.html"

# Gửi yêu cầu GET đến URL
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (status code 200)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích nội dung HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Tìm tất cả các thẻ <td> có nội dung là "Toán"
    toan_td = soup.find("td", string="Toán")
    
    # Kiểm tra xem có thẻ <td> nào chứa thông tin điểm môn Toán không
    if toan_td:
        # Lấy thông tin điểm từ thẻ <td> kế tiếp
        diem_toan = toan_td.find_next_sibling("td").get_text()
        print("Điểm môn Toán:", diem_toan)
    else:
        print("Không tìm thấy thông tin điểm môn Toán")
else:
    print("Yêu cầu không thành công, mã trạng thái:", response.status_code)
