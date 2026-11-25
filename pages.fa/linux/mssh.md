# mssh

> کارخواه SSH مبتنی بر GTK+ برای تعامل هم‌زمان با چند سرور SSH.
> اطلاعات بیشتر: <https://manned.org/mssh>.

- باز کردن پنجرهٔ جدید و اتصال به چند سرور SSH:

`mssh {{user@host1 user@host2 ...}}`

- باز کردن پنجرهٔ جدید و اتصال به گروه سرورهای ازپیش‌تعریف‌شده در `~/.mssh_clusters`:

`mssh {{[-a|--alias]}} {{alias_name}}`
