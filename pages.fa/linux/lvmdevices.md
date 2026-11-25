# lvmdevices

> مدیریت فایل دستگاه‌های LVM که دستگاه‌های بلوکی مجاز برای حجم‌های فیزیکی را فهرست می‌کند.
> اطلاعات بیشتر: <https://manned.org/lvmdevices>.

- فهرست کردن دستگاه‌های ثبت‌شده در فایل دستگاه‌ها:

`sudo lvmdevices`

- افزودن دستگاه به فایل دستگاه‌ها:

`sudo lvmdevices --adddev {{/dev/sdXN}}`

- حذف دستگاه از فایل دستگاه‌ها:

`sudo lvmdevices --deldev {{/dev/sdXN}}`

- افزودن حجم فیزیکی با PVID آن:

`sudo lvmdevices --addpvid {{pvid}}`

- حذف حجم فیزیکی با PVID آن:

`sudo lvmdevices --delpvid {{pvid}}`

- به‌روزرسانی فایل دستگاه‌ها پس از تغییر نام دستگاه‌ها:

`sudo lvmdevices --update`

- بررسی مشکلات فایل دستگاه‌ها:

`sudo lvmdevices --check`

- نمایش نسخه:

`lvmdevices --version`
