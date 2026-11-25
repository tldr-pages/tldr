# semanage permissive

> مدیریت دامنه‌های مجاز پایدار SELinux.
> توجه کنید که این کار عملاً فرایند را بدون محدودیت می‌کند. برای استفادهٔ بلندمدت، پیکربندی صحیح SELinux توصیه می‌شود.
> همچنین : `getenforce`, `setenforce`.
> اطلاعات بیشتر: <https://manned.org/semanage-permissive>.

- فهرست کردن همهٔ انواع فرایند (یا دامنه‌ها) در حالت permissive:

`sudo semanage permissive {{[-l|--list]}}`

- تنظیم حالت permissive برای دامنه:

`sudo semanage permissive {{[-a|--add]}} {{httpd_t}}`

- لغو حالت permissive برای دامنه:

`sudo semanage permissive {{[-d|--delete]}} {{httpd_t}}`
