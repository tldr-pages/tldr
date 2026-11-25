# smbpasswd

> افزودن یا حذف کاربر Samba یا تغییر رمز عبور آن.
> کاربران Samba باید حساب محلی Unix موجود داشته باشند.
> اطلاعات بیشتر: <https://manned.org/smbpasswd.8>.

- تغییر رمز عبور SMB کاربر فعلی:

`smbpasswd`

- افزودن کاربر مشخص به Samba و تنظیم رمز عبور (کاربر باید از قبل در سیستم موجود باشد):

`sudo smbpasswd -a {{username}}`

- تغییر رمز عبور کاربر موجود Samba:

`sudo smbpasswd {{username}}`

- حذف کاربر Samba (اگر حساب Unix حذف شده است به‌جای آن از `pdbedit` استفاده کنید):

`sudo smbpasswd -x {{username}}`
