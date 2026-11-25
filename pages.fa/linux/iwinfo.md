# iwinfo

> دریافت اطلاعات واسط‌های بی‌سیم در OpenWrt.
> اطلاعات بیشتر: <https://openwrt.org/docs/guide-developer/ubus/iwinfo>.

- فهرست کردن همهٔ واسط‌های بی‌سیم موجود:

`iwinfo`

- نمایش اطلاعات مفصل واسط بی‌سیم مشخص:

`iwinfo {{interface}} info`

- پویش شبکه‌های بی‌سیم مجاور قابل مشاهده برای واسط:

`iwinfo {{interface}} scan`

- فهرست کردن دستگاه‌های متصل:

`iwinfo {{interface}} assoclist`

- فهرست کردن کانال‌های پشتیبانی‌شده توسط واسط:

`iwinfo {{interface}} freqlist`

- فهرست کردن سطوح توان ارسال موجود برای واسط:

`iwinfo {{interface}} txpowerlist`

- نمایش راهنما:

`iwinfo h`
