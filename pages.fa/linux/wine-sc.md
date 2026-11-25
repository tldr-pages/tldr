# wine sc

> ایجاد، پرس‌وجو و کنترل سرویس‌های Windows در یک پیشوند Wine.
> بازپیاده‌سازی دستور کنترل سرویس `sc` در Windows است.
> اطلاعات بیشتر: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- پرس‌وجوی وضعیت سرویس:

`wine sc query {{service_name}}`

- ایجاد سرویس جدید از فایل اجرایی (به فاصلهٔ پس از `binpath=` توجه کنید):

`wine sc create {{service_name}} binpath= {{C:\path\to\service.exe}}`

- شروع یا توقف سرویس:

`wine sc {{start|stop}} {{service_name}}`

- تنظیم توضیح سرویس:

`wine sc description {{service_name}} "{{description_text}}"`

- حذف سرویس:

`wine sc delete {{service_name}}`

- نمایش راهنما:

`wine sc /?`
