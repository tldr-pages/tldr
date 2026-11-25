# urpmi.update

> به‌روزرسانی فهرست بسته‌ها از مخزن بسته در Mageia.
> توجه: مستندات Mageia واژه‌های رسانه و مخزن را مترادف به کار می‌برند.
> همچنین : `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> اطلاعات بیشتر: <https://man.linuxreviews.org/man8/urpmi.update.8.html>.

- به‌روزرسانی همهٔ رسانه‌های فعال:

`urpmi.update -a`

- به‌روزرسانی رسانه‌های مشخص (از جمله غیرفعال):

`urpmi.update {{medium1 medium2 ...}}`

- به‌روزرسانی همهٔ رسانه‌های حاوی کلیدواژهٔ مشخص:

`urpmi.update {{keyword}}`

- به‌روزرسانی همهٔ رسانه‌های پیکربندی‌شده:

`urpmi.update e`
