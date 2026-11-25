# lvrename

> تغییر نام حجم منطقی.
> اطلاعات بیشتر: <https://manned.org/lvrename>.

- تغییر نام LV با مسیرهای کامل:

`sudo lvrename {{/dev/vg_name/old_lv}} {{/dev/vg_name/new_lv}}`

- تغییر نام LV با گروه حجم و نام‌ها:

`sudo lvrename {{vg_name}} {{old_lv}} {{new_lv}}`

- پاسخ «بله» به همهٔ پرسش‌ها:

`sudo lvrename {{[-y|--yes]}} {{/dev/vg_name/old_lv}} {{/dev/vg_name/new_lv}}`
