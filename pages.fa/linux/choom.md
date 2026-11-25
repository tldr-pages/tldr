# choom

> نمایش و تغییر مقدار تعدیل امتیاز خاتمه‌دهندهٔ فرایند هنگام کمبود حافظه (OOM).
> اطلاعات بیشتر: <https://manned.org/choom>.

- نمایش امتیاز OOM-killer فرایند با شناسهٔ مشخص:

`choom {{[-p|--pid]}} {{process_id}}`

- تغییر مقدار تعدیل امتیاز OOM-killer یک فرایند مشخص:

`choom {{[-p|--pid]}} {{process_id}} {{[-n|--adjust]}} {{-1000..+1000}}`

- اجرای یک دستور با مقدار تعدیل مشخص برای امتیاز OOM-killer:

`choom {{[-n|--adjust]}} {{-1000..+1000}} {{command}} {{argument1 argument2 ...}}`
