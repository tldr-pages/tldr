# mount.cifs

> سوار کردن اشتراک‌های SMB (بلوک پیام سرور) یا CIFS (فایل‌سیستم اینترنتی مشترک).
> توجه: همین کار را می‌توان با ارسال گزینهٔ `-t cifs` به `mount` نیز انجام داد.
> اطلاعات بیشتر: <https://manned.org/mount.cifs>.

- اتصال با نام کاربری مشخص یا به‌طور پیش‌فرض `$USER` (رمز عبور درخواست می‌شود):

`mount.cifs -o user={{username}} //{{server}}/{{share_name}} {{path/to/mount_point}}`

- اتصال به‌عنوان کاربر مهمان (بدون رمز عبور):

`mount.cifs -o guest //{{server}}/{{share_name}} {{path/to/mount_point}}`

- تنظیم اطلاعات مالکیت دایرکتوری سوارشده:

`mount.cifs -o uid={{user_id|username}},gid={{group_id|groupname}} //{{server}}/{{share_name}} {{path/to/mount_point}}`
