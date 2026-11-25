# flatpak update

> به‌روزرسانی برنامه‌ها و محیط‌های اجرای Flatpak.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-update>.

- به‌روزرسانی همهٔ برنامه‌ها و محیط‌های اجرای نصب‌شده (برای تأیید خودکار همهٔ درخواست‌ها از `-y` استفاده کنید):

`flatpak update`

- به‌روزرسانی فقط یک برنامهٔ مشخص:

`flatpak update {{com.example.app}}`

- به‌روزرسانی یا بازگشت به کامیت مشخص (همچنین flatpak remote-info و flatpak mask را ببینید):

`flatpak update --commit {{COMMIT}} {{com.example.app}}`
