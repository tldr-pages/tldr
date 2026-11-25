# owut

> ابزار ارتقای OpenWrt برای خودکارسازی ساخت و نصب از طریق Attended SysUpgrade (ASU).
> اطلاعات بیشتر: <https://openwrt.org/docs/guide-user/installation/sysupgrade.owut>.

- فهرست کردن نسخه‌های موجود OpenWrt برای دستگاه فعلی:

`owut versions`

- فهرست کردن بسته‌های نصب یا حذف‌شده توسط کاربر:

`owut list`

- بررسی به‌روزرسانی‌ها بدون انجام ارتقا:

`owut check`

- ساخت، بارگیری، بررسی و نصب خودکار جدیدترین میان‌افزار موجود:

`owut upgrade`

- ارتقا به نسخهٔ مشخص و افزودن بسته‌های اضافی:

`owut upgrade {{[-V|--version-to]}} {{version}} {{[-a|--add]}} "{{htop vim}}"`

- بارگیری و بررسی تصویر مشخص بدون نصب آن:

`owut download {{[-V|--version-to]}} {{25.12.0}}`

- بررسی جدیدترین تصویر بارگیری‌شده و نصب آن (دستگاه مجدداً راه‌اندازی می‌شود):

`owut install`
