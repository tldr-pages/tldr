# fsadm

> بررسی یا تغییر اندازهٔ سیستم فایل روی یک دستگاه.
> اطلاعات بیشتر: <https://manned.org/fsadm>.

- بررسی خطاهای سیستم فایل:

`fsadm check {{/dev/vg_name/lv_name}}`

- شبیه‌سازی تغییر اندازه به اندازهٔ مشخص بدون اعمال تغییر:

`fsadm {{[-n|--dry-run]}} resize {{/dev/vg_name/lv_name}} {{10G}}`

- بزرگ کردن سیستم فایل برای پر کردن کل دستگاه (اندازه را مشخص نکنید):

`fsadm resize {{/dev/vg_name/lv_name}}`

- تغییر هم‌زمان اندازهٔ سیستم فایل و حجم منطقی زیرین:

`fsadm {{[-l|--lvresize]}} resize {{/dev/vg_name/lv_name}} {{100G}}`

- برای ext2/3/4، پیاده کردن و تغییر اندازه به‌صورت آفلاین:

`fsadm {{[-e|--ext-offline]}} resize {{/dev/vg_name/lv_name}} {{20G}}`
