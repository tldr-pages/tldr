# Palworld

> ایجاد و شروع سرور بدون رابط گرافیکی Palworld.
> اطلاعات بیشتر: <https://docs.palworldgame.com/settings-and-operation/arguments/>.

- شروع سرور با تنظیمات پیش‌فرض:

`{{path/to}}/PalServer.sh`

- شروع سرور با پورت مشخص و تنظیم حداکثر تعداد بازیکنان:

`{{path/to}}/PalServer.sh -port={{8211}} -players={{1..32}}`

- شروع سرور لابی عمومی:

`{{path/to}}/PalServer.sh -publiclobby`

- شروع سرور با بهینه‌سازی عملکرد برای CPUهای چندرشته‌ای:

`{{path/to}}/PalServer.sh -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS`

- شروع سرور با IP عمومی و پورت مشخص برای سرورهای جامعه:

`{{path/to}}/PalServer.sh -publicip={{ip_address}} -publicport={{port}}`
