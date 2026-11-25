# hostnamectl

> دریافت یا تنظیم نام میزبان رایانه.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/hostnamectl.html>.

- دریافت نام میزبان رایانه:

`hostnamectl`

- تنظیم نام میزبان رایانه:

`sudo hostnamectl set-hostname "{{hostname}}"`

- تنظیم نام میزبان نمایشی برای رایانه:

`sudo hostnamectl set-hostname --static "{{hostname.example.com}}" && sudo hostnamectl set-hostname --pretty "{{hostname}}"`

- بازنشانی نام میزبان به مقدار پیش‌فرض:

`sudo hostnamectl set-hostname --pretty ""`
