# nologin

> پوستهٔ جایگزین که مانع ورود کاربر می‌شود.
> اطلاعات بیشتر: <https://manned.org/nologin.8>.

- تنظیم پوستهٔ ورود کاربر به `nologin` برای جلوگیری از ورود او:

`chsh {{[-s|--shell]}} {{user}} nologin`

- سفارشی‌سازی پیام برای کاربران دارای پوستهٔ ورود `nologin`:

`echo "{{declined_login_message}}" >/etc/nologin.txt`
