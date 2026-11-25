# isoinfo

> ابزارهایی برای استخراج و بررسی تصاویر دیسک ISO.
> اطلاعات بیشتر: <https://manned.org/isoinfo>.

- فهرست کردن همهٔ فایل‌های موجود در تصویر ISO:

`isoinfo -f -i {{path/to/image.iso}}`

- استخراج فایل مشخص از تصویر ISO و ارسال آن به `stdout`:

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- نمایش اطلاعات سربرگ تصویر دیسک ISO:

`isoinfo -d -i {{path/to/image.iso}}`
