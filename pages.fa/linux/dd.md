# dd

> تبدیل و کپی یک فایل.
> همچنین ببینید: `caligula`.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- ایجاد یک درایو USB قابل راه‌اندازی از یک فایل isohybrid (مانند `archlinux-xxx.iso`) و نمایش پیشرفت:

`sudo dd status=progress if={{path/to/file.iso}} of={{/dev/usb_drive}}`

- رونوشت‌گیری از یک درایو به درایوی دیگر با اندازهٔ بلوک ۴ MiB و همگام‌سازی داده‌های نوشته‌شده پیش از پایان دستور:

`sudo dd bs=4M conv=fsync if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- ایجاد یک فایل با تعداد مشخص بایت تصادفی با استفاده از درایور تصادفی هسته:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- ارزیابی عملکرد نوشتن روی یک دیسک:

`dd bs={{1M}} count={{1024}} if=/dev/zero of={{path/to/file_1GB}}`

- ایجاد نسخهٔ پشتیبان سیستم و ذخیره در یک فایل IMG (که بعداً با جابه‌جا کردن `if` و `of` قابل بازیابی است) و نمایش پیشرفت:

`sudo dd status=progress if={{/dev/drive_device}} of={{path/to/file.img}}`

- بررسی پیشرفت یک عملیات `dd` در حال اجرا (این دستور را از پوسته‌ای دیگر اجرا کنید):

`progress`
