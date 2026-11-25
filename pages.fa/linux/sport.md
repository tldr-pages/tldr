# sport

> جست‌وجو و نصب SlackBuildها.
> اطلاعات بیشتر: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- دریافت فهرست SlackBuildها برای اجرای نخست `sport`:

`sudo mkdir {{[-p|--parents]}} /usr/ports && sudo rsync {{[-av|--archive --verbose]}} rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- دریافت به‌روزرسانی‌های درخت سیستم از طریق `rsync`:

`sudo sport rsync`

- جست‌وجوی بسته با نام:

`sport search "{{keyword}}"`

- بررسی نصب بودن بسته:

`sport check {{package}}`

- نمایش فایل‌های README و `.info` بسته:

`sport cat {{package}}`

- نصب بسته پس از برطرف شدن وابستگی‌ها:

`sudo sport install {{package}}`

- نصب فهرست بسته‌ها از فایل (قالب: بسته‌ها با فاصله جدا می‌شوند):

`sudo sport install $(<{{path/to/list}})`
