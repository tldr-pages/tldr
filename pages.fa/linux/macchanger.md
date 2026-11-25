# macchanger

> تغییر آدرس‌های MAC واسط شبکه.
> اطلاعات بیشتر: <https://manned.org/macchanger>.

- مشاهدهٔ آدرس‌های MAC فعلی و دائمی واسط:

`macchanger {{[-s|--show]}} {{interface}}`

- تنظیم MAC تصادفی برای واسط:

`macchanger {{[-r|--random]}} {{interface}}`

- تنظیم آدرس MAC تصادفی برای واسط و وانمود کردن به آدرس سخت‌افزاری ثبت‌شده (burned-in):

`macchanger {{[-r|--random]}} {{[-b|--bia]}} {{interface}}`

- تنظیم آدرس MAC مشخص برای واسط:

`macchanger {{[-m|--mac]}} {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- چاپ شناسه‌های همهٔ سازندگان شناخته‌شده (سه بایت نخست آدرس MAC):

`macchanger {{[-l|--list]}}`

- بازنشانی واسط به آدرس MAC سخت‌افزاری دائمی آن:

`macchanger {{[-p|--permanent]}} {{interface}}`
