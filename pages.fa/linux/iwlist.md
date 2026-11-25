# iwlist

> دریافت اطلاعات مفصل از واسط بی‌سیم.
> اطلاعات بیشتر: <https://manned.org/iwlist>.

- نمایش فهرست نقاط دسترسی و سلول‌های ad-hoc در محدوده:

`iwlist {{wireless_interface}} scan`

- نمایش فرکانس‌های موجود در دستگاه:

`iwlist {{wireless_interface}} frequency`

- فهرست کردن نرخ‌های بیت پشتیبانی‌شده توسط دستگاه:

`iwlist {{wireless_interface}} rate`

- فهرست کردن پارامترهای احراز هویت WPA تنظیم‌شده:

`iwlist {{wireless_interface}} auth`

- فهرست کردن همهٔ کلیدهای رمزگذاری WPA تنظیم‌شده در دستگاه:

`iwlist {{wireless_interface}} wpakeys`

- فهرست کردن اندازه‌های پشتیبانی‌شدهٔ کلید رمزگذاری و همهٔ کلیدهای رمزگذاری تنظیم‌شده در دستگاه:

`iwlist {{wireless_interface}} keys`

- فهرست کردن ویژگی‌ها و حالت‌های مختلف مدیریت توان دستگاه:

`iwlist {{wireless_interface}} power`

- فهرست کردن عناصر اطلاعاتی عمومی تنظیم‌شده در دستگاه (برای پشتیبانی از WPA):

`iwlist {{wireless_interface}} genie`
