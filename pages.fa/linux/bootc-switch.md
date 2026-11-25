# bootc switch

> انتخاب مرجع یک تصویر کانتینر جدید برای راه‌اندازی سیستم.
> اطلاعات بیشتر: <https://manned.org/bootc-switch>.

- تغییر سیستم‌عامل پایه به یک تصویر کانتینر جدید از یک رجیستری:

`sudo bootc switch {{image}}`

- تغییر سیستم‌عامل پایه به یک تصویر کانتینر جدید از فضای ذخیره‌سازی تصاویر محلی کاربر ریشه:

`sudo bootc switch --transport containers-storage {{image}}`

- تغییر سیستم‌عامل پایه به یک تصویر کانتینر جدید ذخیره‌شده در فایل tar:

`sudo bootc switch --transport oci-archive {{path/to/image.tar.gz}}`
