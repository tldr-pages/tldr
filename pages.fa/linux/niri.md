# niri

> ترکیب‌گر Wayland با چیدمان کاشی‌وار قابل پیمایش.
> اطلاعات بیشتر: <https://github.com/YaLTeR/niri>.

- فهرست کردن همهٔ خروجی‌ها و ویژگی‌های آن‌ها:

`niri msg outputs`

- خاموش کردن خروجی (نمایشگر):

`niri msg output {{output_name}} off`

- تمرکز روی فضای کاری زیر فضای فعلی:

`niri msg action focus-workspace-down`

- تمرکز روی فضای کاری بالای فضای فعلی:

`niri msg action focus-workspace-up`

- انتقال فضای کاری فعلی به پایین:

`niri msg action move-workspace-down`

- بستن پنجرهٔ دارای تمرکز فعلی:

`niri msg action close-window`

- تمرکز روی فضای کاری مشخص با شاخص:

`niri msg action focus-workspace {{workspace_index}}`
