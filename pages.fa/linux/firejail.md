# firejail

> ایزوله‌سازی امن فرایندها در کانتینر با استفاده از قابلیت‌های داخلی لینوکس.
> اطلاعات بیشتر: <https://manned.org/firejail>.

- یکپارچه‌سازی firejail با محیط میزکار:

`sudo firecfg`

- باز کردن Mozilla Firefox با محدودیت:

`firejail {{firefox}}`

- شروع سرور آپاچی محدودشده روی رابط و آدرس شناخته‌شده:

`firejail --net={{eth0}} --ip={{192.168.1.244}} {{/etc/init.d/apache2}} {{start}}`

- فهرست کردن محیط‌های ایزولهٔ در حال اجرا:

`firejail --list`

- فهرست کردن فعالیت شبکهٔ محیط‌های ایزولهٔ در حال اجرا:

`firejail --netstats`

- خاموش کردن یک محیط ایزولهٔ در حال اجرا:

`firejail --shutdown={{7777}}`

- اجرای نشست Firefox محدودشده برای مرور اینترنت:

`firejail --seccomp --private --private-dev --private-tmp --protocol=inet firefox --new-instance --no-remote --safe-mode --private-window`

- استفاده از فایل hosts دلخواه به جای فایل `/etc/hosts`:

`firejail --hosts-file={{~/myhosts}} {{curl http://mysite.arpa}}`
