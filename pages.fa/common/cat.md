# cat

> چاپ و ترکیب کردن فایل ها.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/cat>.

- چاپ محتویات فایل بر روی صفحه نمایش:

`cat {{path/to/file}}`

- ادغام چند فایل با هم و ایجاد فایل جدید:

`cat {{path/to/file1 path/to/file2 ...}} > {{target_file}}`

- ادغام چند فایل با هم و اضافه کردن آن به فایل مقصد:

`cat {{path/to/file1 path/to/file2 ...}} >> {{target_file}}`

- شمارش تعداد خط های فایل:

`cat -n {{file}}`

- نمایش محتویات فایل بدون فضای خالی (نا مناسب برای چاپ):

`cat -v -t -e {{file}}`
