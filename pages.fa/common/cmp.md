# cmp

> مقایسه بایت به بایت دو فایل.
> اطلاعات بیشتر: <https://www.gnu.org/software/diffutils/manual/diffutils.html#Invoking-cmp>.

- نمایش کارکتر و خطی که اولین تفاوت دو فایل در آن یافت شد:

`cmp {{path/to/file1}} {{path/to/file2}}`

- نمایش اطلاعات اولین تفاوت پیدا شده: کاراکتر، شماره خط، بایت ها، و مقادیر آنها:

`cmp {{[-b|--print-bytes]}} {{path/to/file1}} {{path/to/file2}}`

- نمایش شماره بایتها و مقادیر تمامی تفاوت ها:

`cmp {{[-l|--verbose]}} {{path/to/file1}} {{path/to/file2}}`

- مقایسه فایلها در حالت خاموش، تنها مقدار خروجی برنامه در ترمینال در دسترس است:

`cmp {{[-s|--quiet]}} {{path/to/file1}} {{path/to/file2}}`
