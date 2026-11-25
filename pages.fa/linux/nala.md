# nala

> ابزار مدیریت بسته با قالب‌بندی بهتر.
> رابطی برای API مربوط به `python-apt`.
> اطلاعات بیشتر: <https://gitlab.com/volian/nala>.

- نصب بسته یا به‌روزرسانی آن به جدیدترین نسخهٔ موجود:

`sudo nala install {{package}}`

- حذف بسته:

`sudo nala remove {{package}}`

- حذف بسته و فایل‌های پیکربندی آن:

`nala purge {{package}}`

- جست‌وجوی نام و توضیحات بسته‌ها با کلمه، `regex` (پیش‌فرض) یا `glob`:

`nala search "{{pattern}}"`

- به‌روزرسانی فهرست بسته‌های موجود و ارتقای سیستم:

`sudo nala upgrade`

- حذف همهٔ بسته‌ها و وابستگی‌های استفاده‌نشده از سیستم:

`sudo nala autoremove`

- دریافت آینه‌های سریع برای بهبود سرعت بارگیری:

`sudo nala fetch`

- نمایش تاریخچهٔ همهٔ تراکنش‌ها:

`nala history`
