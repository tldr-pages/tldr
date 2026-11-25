# opkg

> مدیر بستهٔ سبک برای نصب بسته‌های OpenWrt.
> اطلاعات بیشتر: <https://openwrt.org/docs/guide-user/additional-software/opkg>.

- نصب بسته:

`opkg install {{package}}`

- حذف بسته:

`opkg remove {{package}}`

- به‌روزرسانی فهرست بسته‌های موجود:

`opkg update`

- ارتقای یک یا چند بستهٔ مشخص:

`opkg upgrade {{package1 package2 ...}}`

- نمایش اطلاعات بستهٔ مشخص:

`opkg info {{package}}`

- فهرست کردن همهٔ بسته‌های موجود:

`opkg list`

- یافتن بستهٔ مالک یک فایل:

`opkg search /{{path/to/file}}`

- فهرست کردن همهٔ فایل‌های متعلق به بسته:

`opkg files {{package}}`
