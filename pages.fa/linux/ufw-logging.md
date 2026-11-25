# ufw logging

> پیکربندی ثبت رویدادهای دیوار آتش.
> توجه: سطوح ثبت `high` و `full` ممکن است فضای دیسک را به‌سرعت پر کنند.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- فعال کردن ثبت با سطح پیش‌فرض (low):

`sudo ufw logging on`

- غیرفعال کردن ثبت:

`sudo ufw logging off`

- تنظیم سطح ثبت:

`sudo ufw logging {{low|medium|high|full}}`

- ثبت اتصال‌های جدید (`log`) یا همهٔ بسته‌های مطابق قانون (`log-all`):

`sudo ufw {{allow|deny|reject|limit}} {{log|log-all}} {{22/tcp}}`
