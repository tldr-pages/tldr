# systemd-repart

> افزایش خودکار اندازه و افزودن پارتیشن‌ها.
> بر اساس فایل‌های پیکربندی توصیف‌شده در repart.d پارتیشن‌ها را افزایش و اضافه می‌کند.
> اندازهٔ فایل‌سیستم پارتیشن را خودکار تغییر نمی‌دهد؛ برای گسترش فایل‌سیستم systemd-growfs را ببینید.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-repart.html>.

- گسترش پارتیشن ریشه (/) به همهٔ فضای موجود دیسک:

`systemd-repart`

- شبیه‌سازی پارتیشن‌بندی مجدد و نمایش تغییرات بدون اعمال:

`systemd-repart --dry-run yes`

- افزایش اندازهٔ پارتیشن ریشه به ۱۰ گیگابایت:

`systemd-repart --size 10G --root /`
