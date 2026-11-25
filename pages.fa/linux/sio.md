# sio

> ابزار جامع اطلاعات سخت‌افزار لینوکس و پایش بلادرنگ حسگر.
> اطلاعات بیشتر: <https://github.com/level1techs/siomon>.

- باز کردن رابط متنی Siomon:

`sio`

- تنظیم فاصلهٔ نظرسنجی دلخواه:

`sio --interval {{milliseconds}}`

- ثبت لحظه‌ای مقادیر فعلی حسگر:

`sio sensors`

- خروجی گزارش در نوع فایل مشخص:

`sio {{[-f|--format]}} {{json|xml|html}}`

- خروجی جزئیات سخت‌افزار مشخص:

`sio {{cpu|gpu|memory|storage|network|pci|pcie|audio|usb|battery|board}}`

- باز کردن sio با دسترسی root به حسگر:

`sudo sio`
