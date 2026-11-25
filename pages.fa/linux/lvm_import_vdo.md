# lvm_import_vdo

> وارد کردن حجم VDO ایجادشده توسط مدیر VDO به حجم منطقی مدیریت‌شده توسط LVM (برگشت‌ناپذیر).
> اطلاعات بیشتر: <https://manned.org/lvm_import_vdo>.

- وارد کردن حجم VDO با نام‌های خودکار برای VG/LV:

`lvm_import_vdo {{/dev/mapper/vdo_volume}}`

- وارد کردن و تنظیم نام VG/LV مقصد:

`lvm_import_vdo {{[-n|--name]}} {{vg_name/lv_name}} {{/dev/mapper/vdo_volume}}`

- شبیه‌سازی ورود و نمایش عملیات بدون تغییر چیزی:

`lvm_import_vdo --dry-run {{/dev/mapper/vdo_volume}}`

- تبدیل درجا بدون استفاده از snapshot موقت (با امنیت کمتر):

`lvm_import_vdo --no-snapshot {{/dev/mapper/vdo_volume}}`

- تبدیل حجم VDO با خروجی مفصل و پاسخ خودکار «بله» به پرسش‌ها:

`lvm_import_vdo {{[-v|--verbose]}} {{[-y|--yes]}} {{/dev/mapper/vdo_volume}}`

- استفاده از فایل پیکربندی مدیر VDO هنگام ورود:

`lvm_import_vdo --vdo-config {{path/to/vdo.conf}} {{/dev/mapper/vdo_volume}}`
