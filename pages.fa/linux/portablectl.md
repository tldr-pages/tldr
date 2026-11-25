# portablectl

> ابزار systemd برای مدیریت و استقرار تصاویر سرویس قابل حمل در سیستم‌های لینوکس.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/portablectl.html>.

- فهرست کردن تصاویر سرویس قابل حمل موجود که در مسیرهای جست‌وجوی تصویر شناسایی شده‌اند:

`portablectl list`

- اتصال تصویر سرویس قابل حمل به سیستم میزبان:

`portablectl attach {{path/to/image}}`

- جدا کردن تصویر سرویس قابل حمل از سیستم میزبان:

`portablectl detach {{path/to/image|image_name}}`

- نمایش جزئیات و فرادادهٔ تصویر سرویس قابل حمل مشخص:

`portablectl inspect {{path/to/image}}`

- بررسی اتصال تصویر سرویس قابل حمل به سیستم میزبان:

`portablectl is-attached {{path/to/image|image_name}}`
