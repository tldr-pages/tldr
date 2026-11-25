# urpmi

> نصب بسته‌ها در Mageia.
> همچنین : `urpmi.update`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> اطلاعات بیشتر: <https://man.linuxreviews.org/man8/urpmi.8.html>.

- نصب بسته از مخزن یا فایل RPM محلی:

`sudo urpmi {{package|path/to/file.rpm}}`

- بارگیری بسته بدون نصب:

`urpmi --no-install {{package}}`

- به‌روزرسانی همهٔ بسته‌های نصب‌شده (برای دریافت به‌روزرسانی‌های موجود `urpmi.update -a` را اجرا کنید):

`sudo urpmi --auto-select`

- به‌روزرسانی بستهٔ یک یا چند دستگاه شبکه مطابق `/etc/urpmi/parallel.cfg`:

`sudo urpmi --parallel local {{package}}`

- علامت‌گذاری همهٔ بسته‌های یتیم به‌عنوان نصب‌شده به‌صورت دستی:

`sudo urpmi $(urpmq --auto-orphans -f)`
