# goldeneye.py

> ابزار آزمون منع سرویس HTTP.
> اطلاعات بیشتر: <https://github.com/jseidl/GoldenEye#usage>.

- آزمودن یک وب‌سایت مشخص:

`{{path/to}}/goldeneye.py {{url}}`

- آزمودن یک وب‌سایت مشخص با ۱۰۰ عامل کاربر و ۲۰۰ سوکت هم‌زمان:

`{{path/to}}/goldeneye.py {{url}} {{[-u|--useragents]}} 100 {{[-s|--sockets]}} 200`

- آزمودن یک وب‌سایت مشخص بدون اعتبارسنجی گواهی SSL:

`{{path/to}}/goldeneye.py {{url}} {{[-n|--nosslcheck]}}`

- آزمودن یک وب‌سایت مشخص در حالت اشکال‌زدایی:

`{{path/to}}/goldeneye.py {{url}} {{[-d|--debug]}}`

- نمایش راهنما:

`{{path/to}}/goldeneye.py {{[-h|--help]}}`
