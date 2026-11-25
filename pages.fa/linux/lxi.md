# lxi

> کنترل ابزارهای سازگار با LXI مانند نوسان‌نماها.
> اطلاعات بیشتر: <https://github.com/lxi-tools/lxi-tools#32-lxi>.

- کشف دستگاه‌های LXI در شبکه‌های موجود:

`lxi discover`

- گرفتن تصویر صفحه با شناسایی خودکار افزونه:

`lxi screenshot {{[-a|--address]}} {{ip_address}}`

- گرفتن تصویر صفحه با افزونهٔ مشخص:

`lxi screenshot {{[-a|--address]}} {{ip_address}} {{[-p|--plugin]}} {{rigol-1000z}}`

- ارسال دستور SCPI به ابزار:

`lxi scpi {{[-a|--address]}} {{ip_address}} "{{*IDN?}}"`

- اجرای آزمون عملکرد درخواست و پاسخ:

`lxi benchmark {{[-a|--address]}} {{ip_address}}`
