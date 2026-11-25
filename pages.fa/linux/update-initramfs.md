# update-initramfs

> مدیریت initramfs.
> اطلاعات بیشتر: <https://manned.org/update-initramfs>.

- ایجاد initramfs جدید (برای همهٔ نسخه‌های نصب‌شدهٔ هسته از `all` استفاده کنید):

`sudo update-initramfs -c -k {{kernel_version}}`

- به‌روزرسانی initramfs موجود:

`sudo update-initramfs -u`

- حذف initramfs موجود (هنگام استفاده از `all` برای `kernel_version` احتیاط کنید):

`sudo update-initramfs -d -k {{kernel_version}}`
