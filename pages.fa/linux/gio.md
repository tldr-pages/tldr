# gio

> مدیریت فایل‌های محلی و مجازی (GVfs).
> بخشی از GLib است که در سیستم‌های مبتنی بر GNOME استفاده می‌شود.
> اطلاعات بیشتر: <https://manned.org/gio>.

- باز کردن فایل با برنامهٔ پیش‌فرض (مانند PDF یا تصویر):

`gio open {{path/to/file}}`

- فهرست کردن فایل‌های یک دایرکتوری:

`gio list {{path/to/directory}}`

- نمایش اطلاعات یک فایل:

`gio info {{path/to/file}}`

- کپی کردن یک فایل:

`gio copy {{path/to/source}} {{path/to/destination}}`

- انتقال یک فایل به سطل زباله (قابل بازگشت):

`gio trash {{path/to/file}}`

- خالی کردن سطل زباله:

`gio trash --empty`

- اجرای برنامه از فایل `.desktop`:

`gio launch {{path/to/file}}.desktop`

- علامت‌گذاری فایل `.desktop` به‌عنوان مورد اعتماد و اجازهٔ اجرای آن:

`gio set {{path/to/file}}.desktop metadata::trusted true`
