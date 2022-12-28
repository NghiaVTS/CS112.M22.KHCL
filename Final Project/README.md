Recover license plates
1. Mô tả bài toán:
Ngữ cảnh ứng dụng: giải quyết vấn về input bị mờ, làm giảm độ chính xác cho việc detect biển số xe, 
giúp chuẩn bị dữ liệu hoàn chỉnh hơn cho các bài toán sử dụng biển số xe.

- Input: biển số xe bị mờ, kém chất lượng.
- Output: biển số xe được làm rõ.
- Per matrix: đưa cả input lẫn output vào model detect biển số xe rồi dùng độ chính xác để so sánh.

2. Mô tả bộ dữ liệu:
- Cách thức xây dựng dữ liệu: vì input là ảnh bị mờ nên việc tìm kiếm bộ dataset thỏa nhu cầu là rất khó, 
vậy nên có thể dùng dataset của biển số xe (ảnh rõ, lấy trên kaggle), rồi dùng hàm blur của cv2 để làm mờ 
ảnh.
- Số lượng và độ đa dạng: vì bài toán detect biển số xe là rất phổ biến nên data source có thể lấy 
trên kaggle từ đó build bộ dataset.
-Các thao tác: chia thành 2 generator là fake và real, với fake là ảnh mờ và real là ảnh rõ, có thể dùng
data lấy được từ kaggle để build. Với ảnh fake là ảnh dựa trên ảnh real được dùng effect blur.

3. Mô tả đặc trưng:
- Dựa trên bài image restoration là sử dụng mạng GAN, thì ở đây dùng model pix2pix sử dụng patchGAN.
