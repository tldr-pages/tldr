# xdg-mime

> پرس‌وجو و مدیریت انواع MIME مطابق استاندارد XDG.
> اطلاعات بیشتر: <https://portland.freedesktop.org/doc/xdg-mime.html>.

- نمایش نوع MIME فایل:

`xdg-mime query filetype {{path/to/file}}`

- نمایش برنامهٔ پیش‌فرض باز کردن PNG:

`xdg-mime query default {{image/png}}`

- نمایش برنامهٔ پیش‌فرض باز کردن فایل مشخص:

`xdg-mime query default $(xdg-mime query filetype {{path/to/file}})`

- تنظیم imv به‌عنوان برنامهٔ پیش‌فرض باز کردن تصاویر PNG و JPEG:

`xdg-mime default {{imv.desktop}} {{image/png}} {{image/jpeg}}`
