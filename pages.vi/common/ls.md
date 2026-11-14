# ls

> Liệt kê nội dung thư mục.
> Thông tin thêm: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Liệt kê mỗi tệp trên một dòng:

`ls -1`

- Liệt kê toàn bộ tệp, bao gồm cả tệp ẩn:

`ls {{[-a|--all]}}`

- Đánh dấu phân loại tệp bằng ký hiệu hậu tố (thư mục/, liên kết tượng trưng@, tệp thực thi*, ...):

`ls {{[-F|--classify]}}`

- Liệt kê toàn bộ tệp ở định dạng chi tiết ([l]ong) (quyền, chủ sở hữu, kích thước và ngày sửa đổi):

`ls {{[-la|-l --all]}}`

- Liệt kê ở định dạng chi tiết ([l]ong), hiển thị kích thước bằng đơn vị dễ đọc (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Liệt kê đệ quy ở định dạng chi tiết ([l]ong), sắp xếp theo kích thước ([S]ize) giảm dần:

`ls {{[-lSR|-lS --recursive]}}`

- Liệt kê ở định dạng chi tiết ([l]ong), sắp xếp theo thời gian ([t]ime) sửa đổi đảo ngược (cũ nhất lên trước):

`ls {{[-ltr|-lt --reverse]}}`

- Chỉ liệt kê các thư mục:

`ls {{[-d|--directory]}} */`
