# evtest

> نمایش اطلاعات درایورهای دستگاه ورودی.
> اطلاعات بیشتر: <https://manned.org/evtest>.

- فهرست کردن همهٔ دستگاه‌های ورودی شناسایی‌شده و انتخاب یکی برای پایش:

`sudo evtest`

- نمایش رویدادهای یک دستگاه ورودی مشخص:

`sudo evtest /dev/input/event{{number}}`

- در اختیار گرفتن انحصاری دستگاه و جلوگیری از دریافت رویدادها توسط دیگر کارخواه‌ها:

`sudo evtest --grab /dev/input/event{{number}}`

- پرس‌وجوی وضعیت یک کلید یا دکمهٔ مشخص در دستگاه ورودی:

`sudo evtest --query /dev/input/event{{number}} {{event_type}} {{event_code}}`
