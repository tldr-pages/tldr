# smbget

> ابزاری مانند `wget` برای بارگیری فایل از سرورهای SMB.
> اطلاعات بیشتر: <https://www.samba.org/samba/docs/current/man-html/smbget.1.html>.

- بارگیری فایل از سرور:

`smbget {{smb://server/share/file}}`

- بارگیری بازگشتی اشتراک یا دایرکتوری:

`smbget --recursive {{smb://server/share}}`

- اتصال با نام کاربری و رمز عبور:

`smbget {{smb://server/share/file}} {{[-U|--user]}} {{username%password}}`

- الزام انتقال رمزگذاری‌شده:

`smbget {{smb://server/share/file}} {{[-e|--encrypt]}}`
