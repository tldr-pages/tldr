# sysdig

> عیب‌یابی، تحلیل و کاوش سیستم.
> ضبط، فیلتر و ذخیرهٔ فراخوانی‌های سیستم.
> اطلاعات بیشتر: <https://github.com/draios/sysdig/wiki>.

- ضبط همهٔ رویدادها از سیستم زنده و چاپ روی صفحه:

`sysdig`

- ضبط همهٔ رویدادها از سیستم زنده و ذخیره روی دیسک:

`sysdig {{[-w|--write]}} {{path/to/file}}.scap`

- خواندن رویدادها از فایل و چاپ روی صفحه:

`sysdig {{[-r|--read]}} {{path/to/file}}.scap`

- فیلتر و چاپ همهٔ فراخوانی‌های open اجراشده توسط cat:

`sysdig proc.name=cat and evt.type=open`

- ثبت هر افزونهٔ یافت‌شده و استفاده از dummy به‌عنوان منبع ورودی با ارسال پارامترهای open به آن:

`sysdig -I dummy:'{{parameter}}'`

- فهرست کردن chiselهای موجود:

`sysdig {{[-cl|--list-chisels]}}`

- استفاده از chisel به نام spy_ip برای مشاهدهٔ داده‌های مبادله‌شده با آدرس IP:

`sysdig {{[-c|--chisel]}} spy_ip {{ip_address}}`
