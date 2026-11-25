# enum4linux

> شناسایی اطلاعات ویندوز و Samba از سیستم‌های راه دور.
> اطلاعات بیشتر: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- تلاش برای شناسایی با همهٔ روش‌ها:

`enum4linux -a {{remote_host}}`

- شناسایی با اعتبارنامه‌های ورود مشخص:

`enum4linux -u {{user_name}} -p {{password}} {{remote_host}}`

- فهرست کردن نام‌های کاربری یک میزبان مشخص:

`enum4linux -U {{remote_host}}`

- فهرست کردن منابع اشتراکی:

`enum4linux -S {{remote_host}}`

- دریافت اطلاعات سیستم‌عامل:

`enum4linux -o {{remote_host}}`
