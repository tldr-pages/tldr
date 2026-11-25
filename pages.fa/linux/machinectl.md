# machinectl

> کنترل مدیر ماشین systemd.
> اجرای عملیات روی ماشین‌های مجازی، کانتینرها و تصاویر.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/machinectl.html>.

- شروع ماشین به‌عنوان سرویس با استفاده از `systemd-nspawn`:

`sudo machinectl start {{machine_name}}`

- توقف ماشین در حال اجرا:

`sudo machinectl stop {{machine_name}}`

- نمایش فهرست ماشین‌های در حال اجرا:

`machinectl list`

- باز کردن پوستهٔ تعاملی داخل ماشین:

`sudo machinectl shell {{machine_name}}`
