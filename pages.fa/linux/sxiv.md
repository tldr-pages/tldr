# sxiv

> نمایشگر سادهٔ تصویر X.
> اطلاعات بیشتر: <https://manned.org/sxiv>.

- باز کردن تصویر:

`sxiv {{path/to/image}}`

- باز کردن تصویر در حالت تمام‌صفحه:

`sxiv -f {{path/to/file}}`

- باز کردن فهرست تصاویر جداشده با خط جدید و خواندن نام فایل‌ها از `stdin`:

`echo {{path/to/file}} | sxiv -i`

- باز کردن یک یا چند تصویر به‌صورت نمایش اسلاید:

`sxiv -S {{seconds}} {{path/to/image1 path/to/image2 ...}}`

- باز کردن یک یا چند تصویر در حالت بندانگشتی:

`sxiv -t {{path/to/image1 path/to/image2 ...}}`
