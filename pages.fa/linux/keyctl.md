# keyctl

> تغییر حلقهٔ کلید هستهٔ لینوکس.
> اطلاعات بیشتر: <https://manned.org/keyctl>.

- فهرست کردن کلیدهای حلقهٔ کلید مشخص:

`keyctl list {{target_keyring}}`

- فهرست کردن کلیدهای فعلی نشست پیش‌فرض کاربر:

`keyctl list {{@us}}`

- ذخیرهٔ کلید در حلقهٔ کلید مشخص:

`keyctl add {{type_keyring}} {{key_name}} {{key_value}} {{target_keyring}}`

- ذخیرهٔ کلید با مقدار دریافتی از `stdin`:

`echo -n {{key_value}} | keyctl padd {{type_keyring}} {{key_name}} {{target_keyring}}`

- تنظیم مهلت انقضا برای کلید:

`keyctl timeout {{key_name}} {{timeout_in_seconds}}`

- خواندن کلید و قالب‌بندی آن به‌صورت نمایش شانزده‌شانزدهی در صورت چاپ‌ناپذیر بودن:

`keyctl read {{key_name}}`

- خواندن کلید و نمایش آن بدون تغییر قالب:

`keyctl pipe {{key_name}}`

- ابطال کلید و جلوگیری از هرگونه عمل بیشتر روی آن:

`keyctl revoke {{key_name}}`
