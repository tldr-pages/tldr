# lvconvert

> تبدیل یا تغییر نوع، افزونگی یا وضعیت حجم‌های منطقی.
> اطلاعات بیشتر: <https://manned.org/lvconvert>.

- تبدیل حجم منطقی خطی به RAID1 (افزودن یک آینه: در مجموع دو نسخه):

`sudo lvconvert --type raid1 {{[-m|--mirrors]}} 1 {{/dev/vg_name/lv_name}}`

- حذف آینه‌سازی و تبدیل مجدد به حجم منطقی خطی:

`sudo lvconvert {{[-m|--mirrors]}} 0 {{/dev/vg_name/lv_name}}`

- ادغام snapshot در حجم منطقی مبدأ آن (در فعال‌سازی بعدی اعمال می‌شود):

`sudo lvconvert --merge {{/dev/vg_name/snapshot_lv}}`

- تعمیر حجم منطقی RAID معیوب:

`sudo lvconvert --repair {{/dev/vg_name/lv_name}}`

- تبدیل حجم منطقی موجود به استخر thin با LV فرادادهٔ جداگانه:

`sudo lvconvert --type thin-pool --poolmetadata {{/dev/vg_name/pool_metadata_lv}} {{/dev/vg_name/pool_lv}}`
