# qm migrate

> مهاجرت ماشین مجازی.
> برای ایجاد کار مهاجرت جدید استفاده می‌شود.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_migrate>.

- مهاجرت ماشین مجازی مشخص:

`qm {{[mi|migrate]}} {{100}} {{target}}`

- جایگزینی محدودیت فعلی پهنای باند ورودی/خروجی با ۱۰ KiB/s:

`qm {{[mi|migrate]}} {{100}} {{target}} --bwlimit 10`

- اجازهٔ مهاجرت ماشین‌های مجازی استفاده‌کننده از دستگاه‌های محلی (فقط root):

`qm {{[mi|migrate]}} {{100}} {{target}} --force true`

- استفاده از مهاجرت آنلاین یا زنده در صورت اجرای ماشین مجازی:

`qm {{[mi|migrate]}} {{100}} {{target}} --online true`

- فعال کردن مهاجرت زندهٔ فضای ذخیره‌سازی برای دیسک‌های محلی:

`qm {{[mi|migrate]}} {{100}} {{target}} --with-local-disks true`
