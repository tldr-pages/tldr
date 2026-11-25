# tomb

> مدیریت دایرکتوری‌های ذخیره‌سازی رمزگذاری‌شده که می‌توان آن‌ها را ایمن جابه‌جا و در فایل‌سیستم پنهان کرد.
> اطلاعات بیشتر: <https://dyne.org/docs/tomb/manpage/>.

- ایجاد tomb جدید با اندازهٔ اولیهٔ ۱۰۰ MB:

`tomb dig -s 100 {{encrypted_directory.tomb}}`

- ایجاد فایل کلید جدید برای قفل کردن tomb؛ رمز عبور کلید از کاربر پرسیده می‌شود:

`tomb forge {{encrypted_directory.tomb.key}}`

- ایجاد اجباری کلید جدید حتی اگر tomb ساخت کلید را مجاز نکند (به‌دلیل swap):

`tomb forge {{encrypted_directory.tomb.key}} -f`

- مقداردهی اولیه و قفل tomb خالی با کلید ساخته‌شده توسط `forge`:

`tomb lock {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- سوار کردن tomb (به‌طور پیش‌فرض در `/media`) با کلید آن برای استفاده مانند دایرکتوری معمولی فایل‌سیستم:

`tomb open {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- بستن tomb (اگر فرایندی از آن استفاده کند شکست می‌خورد):

`tomb close {{encrypted_directory.tomb}}`

- بستن اجباری همهٔ tombهای باز و پایان دادن به برنامه‌های استفاده‌کننده:

`tomb slam all`

- فهرست کردن همهٔ tombهای باز:

`tomb list`
