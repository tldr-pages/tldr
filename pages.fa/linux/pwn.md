# pwn

> کتابخانهٔ توسعهٔ اکسپلویت برای نمونه‌سازی سریع.
> اطلاعات بیشتر: <https://docs.pwntools.com/en/stable/commandline.html>.

- تبدیل کد اسمبلی داده‌شده به `bytes`:

`pwn asm "{{xor edi, edi}}"`

- ایجاد الگوی چرخه‌ای با تعداد نویسهٔ مشخص:

`pwn cyclic {{number}}`

- رمزگذاری داده‌های داده‌شده در مبنای شانزده‌شانزدهی:

`pwn hex {{deafbeef}}`

- رمزگشایی داده‌های داده‌شده از شانزده‌شانزدهی:

`pwn unhex {{6c4f7645}}`

- چاپ shellcode لینوکس x64 برای اجرای پوسته:

`pwn shellcraft {{amd64.linux.sh}}`

- بررسی تنظیمات امنیتی دودویی فایل ELF مشخص:

`pwn checksec {{path/to/file}}`

- بررسی به‌روزرسانی‌های Pwntools:

`pwn update`

- نمایش نسخه:

`pwn version`
