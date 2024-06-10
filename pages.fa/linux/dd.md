# dd

> تبدیل و کپی یک فایل.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/dd>.

- ساخت یک درایو USB قابل بوت از یک فایل iso (مثل `archlinux-xxx.iso`) و نمایش پیشرفت:

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- کلون کردن یک درایو به یک درایو دیگر با اندازهٔ بلوک ۴ مگابایت و اعمال چیزهای نوشته شده پیش از خاتمهٔ دستور:

`dd bs=4M conv=fsync if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- ایجاد یک فایل با تعداد مشخصی بایت تصادفی با استفاده از درایور random کرنل:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- ارزیابی عملکرد نوشتن روی یک دیسک:

`dd bs={{1M}} count={{1000000}} if=/dev/zero of={{path/to/file_1GB}}`

- ساخت یک پشتیبان از سامانه و ذخیرهٔ آن در یک فایل IMG (می‌توان بعداً با تغییر `if` به `of` آن را بازسازی کرد):

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`

- بررسی پیشرفت یک عملکرد در حال اجرای `dd` (این دستور را از یک پوستهٔ دیگر اجرا کنید):

`kill -USR1 $(pgrep -x dd)`
