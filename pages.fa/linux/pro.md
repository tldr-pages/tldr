# pro

> مدیریت سرویس‌های Ubuntu Pro.
> اطلاعات بیشتر: <https://manned.org/ubuntu-advantage>.

- اتصال سیستم به قرارداد پشتیبانی Ubuntu Pro:

`sudo pro attach`

- نمایش وضعیت سرویس‌های Ubuntu Pro:

`pro status`

- بررسی تأثیرپذیری سیستم از آسیب‌پذیری مشخص (و اعمال اصلاح در صورت امکان):

`pro fix {{CVE-number}}`

- نمایش تعداد بسته‌های پشتیبانی‌نشده:

`pro security-status`

- فهرست کردن بسته‌هایی که دیگر برای بارگیری موجود نیستند:

`pro security-status --unavailable`

- فهرست کردن بسته‌های شخص ثالث:

`pro security-status --thirdparty`
