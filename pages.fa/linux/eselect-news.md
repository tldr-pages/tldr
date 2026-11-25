# eselect news

> ماژول `eselect` برای خواندن اخبار جنتو.
> توجه: Portage هنگام همگام‌سازی مخزن، در صورت وجود خبر خوانده‌نشده، اعلانی چاپ می‌کند.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Eselect#News>.

- فهرست کردن اخبار موجود همراه با شمارهٔ آن‌ها (به‌صورت پیش‌فرض همه):

`eselect news list {{all|new}}`

- چاپ اخبار مشخص‌شده:

`eselect news read {{number1 number2 ...}}`

- چاپ همهٔ اخبار خوانده‌نشده:

`eselect news read`

- علامت‌گذاری اخبار مشخص‌شده به‌عنوان خوانده‌نشده:

`eselect news unread {{number1 number2 ...}}`

- حذف همهٔ اخبار خوانده‌شده:

`eselect news purge`

- چاپ تعداد اخبار موجود (به‌صورت پیش‌فرض اخبار جدید):

`eselect news count {{all|new}}`
