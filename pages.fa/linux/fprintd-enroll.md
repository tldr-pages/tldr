# fprintd-enroll

> ثبت اثر انگشت‌ها در پایگاه داده.
> اطلاعات بیشتر: <https://manned.org/fprintd-enroll>.

- ثبت انگشت اشارهٔ دست راست برای کاربر فعلی:

`fprintd-enroll`

- ثبت یک انگشت مشخص برای کاربر فعلی:

`fprintd-enroll {{[-f|--finger]}} {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|...}}`

- ثبت انگشت اشارهٔ دست راست برای کاربر مشخص:

`fprintd-enroll {{username}}`

- ثبت یک انگشت مشخص برای کاربر مشخص:

`fprintd-enroll {{[-f|--finger]}} {{finger_name}} {{username}}`

- نمایش راهنما:

`fprintd-enroll --help`
