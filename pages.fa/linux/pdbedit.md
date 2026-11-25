# pdbedit

> ویرایش پایگاه دادهٔ کاربران Samba.
> برای افزودن یا حذف سادهٔ کاربر و رمز عبور می‌توانید از `smbpasswd` نیز استفاده کنید.
> اطلاعات بیشتر: <https://manned.org/pdbedit>.

- فهرست کردن همهٔ کاربران Samba:

`sudo pdbedit {{[-L|--list]}}`

- فهرست کردن همهٔ کاربران Samba و تنظیمات آن‌ها:

`sudo pdbedit {{[-L|--list]}} {{[-v|--verbose]}}`

- افزودن کاربر موجود Unix به Samba (رمز عبور درخواست می‌شود):

`sudo pdbedit {{[-u|--user]}} {{username}} {{[-a|--create]}}`

- حذف کاربر Samba:

`sudo pdbedit {{[-u|--user]}} {{username}} {{[-x|--delete]}}`

- بازنشانی شمارندهٔ تلاش ناموفق رمز عبور کاربر Samba:

`sudo pdbedit {{[-u|--user]}} {{username}} {{[-z|--bad-password-count-reset]}}`
