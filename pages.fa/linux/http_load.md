# http_load

> ابزار ارزیابی عملکرد HTTP.
> چند دریافت HTTP را به‌صورت موازی برای آزمودن توان عملیاتی وب‌سرور اجرا می‌کند.
> اطلاعات بیشتر: <https://www.acme.com/software/http_load/>.

- شبیه‌سازی ۲۰ درخواست در ثانیه بر اساس فایل فهرست URL مشخص به مدت ۶۰ ثانیه:

`http_load -rate {{20}} -seconds {{60}} {{path/to/urls.txt}}`

- شبیه‌سازی ۵ درخواست هم‌زمان بر اساس فایل فهرست URL مشخص به مدت ۶۰ ثانیه:

`http_load -parallel {{5}} -seconds {{60}} {{path/to/urls.txt}}`

- شبیه‌سازی ۱۰۰۰ درخواست با نرخ ۲۰ درخواست در ثانیه بر اساس فایل فهرست URL مشخص:

`http_load -rate {{20}} -fetches {{1000}} {{path/to/urls.txt}}`

- شبیه‌سازی ۱۰۰۰ درخواست با ۵ درخواست هم‌زمان بر اساس فایل فهرست URL مشخص:

`http_load -parallel {{5}} -fetches {{1000}} {{path/to/urls.txt}}`
