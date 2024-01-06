# logcat

> تخلیه یک لاگ از پیاهم های سیستمی، شامل پشته رهگیری زمان وقوع خطا، و اطلاعات پیام های لاگ شده توسط برنامه ها.
> اطلاعات بیشتر: <https://developer.android.com/studio/command-line/logcat>.

- نمایش لاگ سیستمی :

`logcat`

- نوشتن لاگ سیستمی به یک فایل :

`logcat -f {{path/to/file}}`

- نمایش خطاهای منطبق با الگوی ورودی :

`logcat --regex {{regular_expression}}`

- نمایش لاگ های مربوط به یک PID مشخص :

`logcat --pid={{pid}}`

- نمایش لاگ های پروسه های مربوط به یک بسته مشخص :

`logcat --pid=$(pidof -s {{package}})`
