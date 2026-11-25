# bluetoothd

> سرویس مدیریت دستگاه‌های بلوتوث.
> اطلاعات بیشتر: <https://manned.org/bluetoothd>.

- شروع سرویس:

`bluetoothd`

- شروع سرویس با ثبت گزارش در خروجی استاندارد `stdout`:

`bluetoothd {{[-n|--nodetach]}}`

- شروع سرویس با یک فایل پیکربندی مشخص (پیش‌فرض `/etc/bluetooth/main.conf` است):

`bluetoothd {{[-f|--configfile]}} {{path/to/file}}`

- شروع سرویس با خروجی مفصل در خروجی خطای استاندارد `stderr`:

`bluetoothd {{[-d|--debug]}}`

- شروع سرویس با خروجی مفصل از فایل‌های مشخص در کد منبع bluetoothd یا افزونه‌ها:

`bluetoothd {{[-d|--debug=]}}{{path/to/file1:path/to/file2:...}}`
