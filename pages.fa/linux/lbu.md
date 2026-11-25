# lbu

> مدیریت فایل‌های overlay مربوط به `apk` در سیستم Alpine Linux بدون دیسک.
> توجه: زیردستورهایی مانند `include` در `/etc` می‌نویسند که در RAM ذخیره می‌شود. برای ذخیرهٔ تغییرات باید `lbu commit` را اجرا کنید.
> اطلاعات بیشتر: <https://wiki.alpinelinux.org/wiki/Alpine_local_backup>.

- ثبت تغییرات در ذخیره‌سازی پایدار (به‌طور پیش‌فرض فقط فایل‌های `/etc`):

`lbu {{[ci|commit]}}`

- فهرست کردن فایل‌هایی که با `commit` ذخیره خواهند شد:

`lbu {{[st|status]}}`

- نمایش تغییرات فایل‌های تحت پیگیری که با `commit` ذخیره خواهند شد:

`lbu diff`

- گنجاندن فایل یا دایرکتوری مشخص در overlay مربوط به `apk`:

`lbu {{[inc|include]}} {{path/to/file_or_directory}}`

- مستثنا کردن فایل یا دایرکتوری مشخص در `/etc` از overlay مربوط به `apk`:

`lbu {{[ex|exclude]}} {{path/to/file_or_directory}}`

- نمایش فهرست فایل‌های دستی گنجانده یا مستثناشده:

`lbu {{include|exclude}} -l`

- فهرست کردن پشتیبان‌ها (overlayهای قبلاً ایجادشده):

`lbu {{[lb|list-backup]}}`

- بازگشت به overlay پشتیبان:

`lbu revert {{overlay_filename.tar.gz}}`
