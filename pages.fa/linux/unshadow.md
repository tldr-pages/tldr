# unshadow

> ابزار پروژهٔ John the Ripper برای به‌دست آوردن فایل رمز عبور سنتی Unix اگر سیستم از رمزهای shadow استفاده کند.
> اطلاعات بیشتر: <https://www.openwall.com/john/doc/>.

- ترکیب `/etc/shadow` و `/etc/passwd` سیستم فعلی:

`sudo unshadow /etc/passwd /etc/shadow`

- ترکیب دو فایل دلخواه shadow و رمز عبور:

`sudo unshadow {{path/to/passwd}} {{path/to/shadow}}`
