# systemd-id128

> تولید و چاپ شناسه‌های sd-128.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-id128.html>.

- تولید شناسهٔ تصادفی جدید:

`systemd-id128 new`

- چاپ شناسهٔ دستگاه فعلی:

`systemd-id128 machine-id`

- چاپ شناسهٔ راه‌اندازی فعلی:

`systemd-id128 boot-id`

- چاپ شناسهٔ فراخوانی سرویس فعلی (در سرویس‌های systemd موجود است):

`systemd-id128 invocation-id`

- تولید شناسهٔ تصادفی جدید و چاپ به‌صورت UUID (پنج گروه رقم جداشده با خط تیره):

`systemd-id128 new {{[-u|--uuid]}}`
