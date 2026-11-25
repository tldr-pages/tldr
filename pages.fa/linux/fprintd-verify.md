# fprintd-verify

> تأیید اثر انگشت‌ها در برابر پایگاه داده.
> اطلاعات بیشتر: <https://manned.org/fprintd-verify>.

- تأیید همهٔ اثر انگشت‌های ذخیره‌شدهٔ کاربر فعلی:

`fprintd-verify`

- تأیید اثر انگشت مشخص برای کاربر فعلی:

`fprintd-verify {{[-f|--finger]}} {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|...}}`

- تأیید اثر انگشت‌های کاربر مشخص:

`fprintd-verify {{username}}`

- تأیید اثر انگشت مشخص برای کاربر مشخص:

`fprintd-verify {{[-f|--finger]}} {{finger_name}} {{username}}`

- ناموفق کردن فرایند اگر اثر انگشت با موارد ذخیره‌شده برای کاربر فعلی در پایگاه داده مطابقت نداشته باشد:

`fprintd-verify --g-fatal-warnings`

- نمایش راهنما:

`fprintd-verify {{[-h|--help]}}`
