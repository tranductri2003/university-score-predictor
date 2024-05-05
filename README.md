# Giới thiệu nhóm
## Thành viên nhóm
##### Họ và tên: Trần Đức Trí - mssv: 102210096
##### Họ và tên: Phạm Nguyễn Anh Phát - mssv: 102210302
##### Họ và tên: Lê Anh Tuấn - mssv: 102210097
## Phân công nhiệm vụ
##### Phạm Nguyễn Anh Phát: Crawl dữ liệu và trực quan hóa dữ liệu thô
##### Lê Anh Tuấn: Làm sạch và chuẩn hóa dữ liệu, trực quan hóa dữ liệu sau khi làm sạch
##### Trần Đức Trí: Trực quan hoá mối quan hệ đa biến, phân tích và đưa ra nhận xét  

# Giới thiệu đề tài
1. Mở đầu:
Trong thời đại công nghệ thông tin phát triển mạnh mẽ như hiện nay, việc sử dụng dữ liệu để hiểu và dự đoán các hiện tượng xã hội là không thể phủ nhận. Trong lĩnh vực giáo dục, việc nắm bắt yếu tố ảnh hưởng đến kết quả học tập của học sinh là vô cùng quan trọng để có những chính sách và biện pháp phát triển giáo dục hiệu quả.

2. Bối cảnh nghiên cứu:
Kỳ thi trung học phổ thông Quốc gia (THPTQG) được xem là cột mốc quan trọng đánh giá năng lực học thuật của học sinh trước khi bước vào đại học. Việc hiểu rõ các yếu tố ảnh hưởng đến kết quả của kỳ thi này sẽ giúp chúng ta có cái nhìn tổng quan về chất lượng giáo dục ở mỗi địa phương cũng như từ đó có những đề xuất cải thiện chất lượng giáo dục.

3. Mục tiêu nghiên cứu:

Phân tích các yếu tố ảnh hưởng đến điểm thi trung học phổ thông Quốc gia.
Nghiên cứu sự khác biệt về các yếu tố này giữa các địa phương khác nhau.
Đề xuất các biện pháp cải thiện chất lượng giáo dục dựa trên kết quả phân tích.
- Phân tích các yếu tố xã hội ảnh hưởng đến điểm thi trung học phổ thông Quốc gia.

- Nghiên cứu sự khác biệt về các yếu tố này giữa các địa phương khác nhau.

- Đề xuất các biện pháp cải thiện chất lượng giáo dục dựa trên kết quả phân tích.
# Cấu Trúc thư mục
- [Part 1] Data_Crawling_And_Visualizaton
- [Part 2] Clean Data and Visualize
- [Part 3] Multivariate_Relationship_Analysis
- DATA
  - CLEAN_DATA
  - RAW_DATA
## Gồm 4 thư mục chính:
- ### [Part 1] Data_Crawling_And_Visualizaton :
  Trình bày cách lấy dữ liệu từ các trang web về và trực quan hóa dữ liệu thô để có cái nhìn tổng quan về dữ liệu.
- ### [Part 2] Clean Data and Visualize :
  Làm sạch từng dữ liệu, trình bày cách trực quan hóa các dữ liệu đơn biến sau khi làm sạch.
- ### [Part 3] Multivariate_Relationship_Analysis :
  Lựa chọn, đưa ra mỗi quan hệ đa biến giữa các dữ liệu với nhau, phân tích từng mối quan hệ, đưa ra nhận xét và giải pháp.
- ### Data: Thư mục chứ các dữ liệu
  - RAW DATA: Dữ liệu thô và file lấy dữ liệu
  - CLEAN DATA: Dữ liệu sau khi làm sạch
# Hướng dẫn chạy chương Trình
## Bước 1
 - Vào file Raw Data, trong từng thư mục chạy từng file để đuôi .py để lấy dữ liệu từ web
 - với thư mục "Dân số và mật độ dân số " khi chạy sẽ hiện lên trang web, chọn lọc dữ liệu theo mình cần rồi bấm lọc sau đó dữ liệu sẽ tự lấy về ( có 1000 giây để thực hiện)
 - Tương tự với các file còn lại chỉ cần chạy dữ liệu sẽ tự đổ về
 -  các file không có đuôi .py dữ liệu được lấy bằng thủ công, bạn hãy tự tải về rồi tách ra
## Bước 2:
 - Với từng thư mục trong mục CLEAN DATA hãy chạy file có đuổi .py trong đó để làm sạch từng loại dữ liệu
 - Dữ liệu sau khi làm sạch sẽ được lưu tại chính folder đó.
## Bước 3:
 - Vào thư mục [Part 1] : chạy lần lược từng shell cho đến hết, với mục 1 phần lấy data sẽ giống với bên RAW DATA nhưng là thành 1 pipeline cho dễ nhìn và có thêm mục trực quan hóa.
 - Vào thư mục [Part 2] : chạy lần lược từng shell cho đến hết, với mục 2 phần lấy data sẽ giống với bên RAW DATA nhưng là thành 1 pipeline cho dễ nhìn và có thêm phần chuẩn hóa dữ liệu và trực quan hóa. 
 - Vào thư mục [Part 3] : chạy lần lược từng shell cho đến hết xem kết quả