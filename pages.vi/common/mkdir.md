# mkdir

> Tạo thư mục và thiết lập quyền truy cập.
> Thông tin thêm: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Tạo các thư mục chỉ định:

`mkdir {{đường_dẫn/đến/thư_mục1 đường_dẫn/đến/thư_mục2 ...}}`

- Tạo các thư mục chỉ định cùng các thư mục cha nếu chưa có:

`mkdir {{[-p|--parents]}} {{đường_dẫn/đến/thư_mục1 đường_dẫn/đến/thư_mục2 ...}}`

- Tạo thư mục kèm thiết lập quyền truy cập cụ thể:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{đường_dẫn/đến/thư_mục1 đường_dẫn/đến/thư_mục2 ...}}`

- Tạo đệ quy nhiều thư mục lồng nhau:

`mkdir {{[-p|--parents]}} {{đường_dẫn/đến/{a,b}/{x,y,z}/{h,i,j}}}`
