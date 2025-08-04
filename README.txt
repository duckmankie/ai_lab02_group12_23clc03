

HƯỚNG DẪN CHẠY CHƯƠNG TRÌNH GIẢI BÀI TOÁN CẦU NỐI (HASHIWOKAKERO)

1. Yêu cầu môi trường
- Python 3.8 trở lên
- Các thư viện ngoài: sympy, python-sat

2. Cài đặt thư viện
Chạy lệnh sau trong thư mục project:
pip install -r requirements.txt

3. Cấu trúc thư mục
- main.py: Chương trình chính, giao diện chọn phương pháp giải.
- helper_01.py: các hàm phụ trợ, đọc/viết matrix, convert cnf.
- Inputs/: Thư mục chứa file input (ví dụ: input-01.txt).
- Outputs/: Thư mục chứa file output (ví dụ: output-01.txt).
- requirements.txt: Danh sách thư viện cần cài.

4. Cách chạy chương trình
Chạy lệnh sau trong terminal:
python main.py

Sau đó, chọn phương pháp giải theo menu:
- 1: SAT
- 2: A*
- 3: Brute-force
- 4: Backtracking
- 0: Thoát

Chương trình sẽ đọc input từ Inputs/input-XX.txt và ghi kết quả ra Outputs/output-XX.txt.

5. Định dạng file input/output
- Input: Ma trận số nguyên, mỗi dòng là một hàng, các số cách nhau bởi dấu phẩy, ví dụ:
  0, 0, 1, 0, 0
  0, 0, 0, 0, 0
  1, 0, 4, 0, 3
  0, 0, 0, 0, 0
  0, 0, 1, 0, 2
- Output: Ma trận kết quả, có thể chứa số và ký tự cầu nối (-, =, |, $), ví dụ:
  0, 0, 1, 0, 0
  0, 0, |, 0, 0
  1, -, 4, -, 3
  0, 0, |, 0, $
  0, 0, 1, 0, 2

6. Ý nghĩa các phương pháp giải
- SAT: Dùng bộ giải SAT để tìm lời giải.
- A: Dùng thuật toán A* (tìm kiếm theo heuristic).
- Brute-force: Duyệt vét cạn tất cả các khả năng.
- Backtracking: Quay lui, thử từng khả năng và quay lại khi gặp bế tắc.

7. Ghi chú
- Có thể thêm file input khác vào thư mục (Inputs/) và sửa lại đường dẫn trong main.py nếu muốn test.
- Kết quả sẽ được ghi đè vào file output tương ứng.
