# lvmpersist

> مدیریت رزروهای پایدار (PR) روی دستگاه‌های بلوکی یا همهٔ PVهای یک گروه حجم.
> اطلاعات بیشتر: <https://manned.org/lvmpersist>.

- شروع PR روی همهٔ PVهای یک VG با کلید محلی (به‌طور پیش‌فرض دسترسی انحصاری):

`lvmpersist start --ourkey {{0x1234abcd}} --vg {{vg_name}}`

- شروع PR برای VG اشتراکی (اجازه به چند میزبان):

`lvmpersist start --ourkey {{0x1234abcd}} --access {{sh}} --vg {{vg_name}}`

- توقف PR روی VG و لغو ثبت کلید محلی:

`lvmpersist stop --ourkey {{0x1234abcd}} --vg {{vg_name}}`

- به‌دست گرفتن VG محلی با کنار زدن میزبان دیگر هنگام شروع PR:

`lvmpersist start --ourkey {{0xmy_key}} --removekey {{0xother_key}} --vg {{vg_name}}`

- حذف کلید میزبان دیگر از VG اشتراکی:

`lvmpersist remove --ourkey {{0xmy_key}} --removekey {{0xother_key}} --vg {{vg_name}}`

- نمایش کلیدهای ثبت‌شده و رزروهای یک VG:

`lvmpersist read --vg {{vg_name}}`

- عمل روی دستگاه‌های مشخص به‌جای VG:

`lvmpersist start --ourkey {{0x1234abcd}} --device {{/dev/sdX}} --device {{/dev/mapper/mpathY}}`
