# scrun

> پراکسی محیط اجرای OCI برای Slurm که کانتینرها را به‌صورت کار اجرا می‌کند.
> اطلاعات بیشتر: <https://slurm.schedmd.com/scrun.html>.

- ایجاد کانتینر جدید با شناسهٔ مشخص:

`scrun create {{container_id}}`

- شروع کانتینر قبلاً ایجادشده:

`scrun start {{container_id}}`

- پرس‌وجوی وضعیت کانتینر:

`scrun state {{container_id}}`

- ارسال سیگنال به کانتینر (پیش‌فرض `SIGTERM`):

`scrun kill {{container_id}}`

- ارسال سیگنال مشخص به کانتینر:

`scrun kill {{container_id}} {{SIGKILL}}`

- حذف کانتینر و آزاد کردن منابع آن:

`scrun delete {{container_id}}`

- فعال کردن ثبت گزارش اشکال‌زدایی:

`scrun {{create|start|kill|delete}} {{container_id}} --debug`

- نمایش نسخه:

`scrun --version`
