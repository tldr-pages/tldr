# criu

> متوقف و ذخیره کردن یک برنامهٔ در حال اجرا یا درخت فرایند و بازیابی آن در زمانی دیگر.
> اطلاعات بیشتر: <https://manned.org/criu>.

- بررسی پشتیبانی هستهٔ فعلی از قابلیت‌های لازم CRIU:

`sudo criu check`

- ثبت نقطهٔ بازیابی یک فرایند با شناسهٔ مشخص و ذخیرهٔ وضعیت در دایرکتوری مشخص:

`sudo criu dump {{[-t|--tree]}} {{process_id}} {{[-D|--images-dir]}} {{path/to/directory}}`

- بازیابی یک فرایند از فایل‌های تصویر ذخیره‌شدهٔ قبلی:

`sudo criu restore {{[-D|--images-dir]}} {{path/to/directory}}`

- ذخیرهٔ وضعیت یک فرایند و اجازهٔ ادامهٔ اجرا به جای خاتمه دادن به آن:

`sudo criu dump {{[-t|--tree]}} {{process_id}} {{[-D|--images-dir]}} {{path/to/directory}} {{[-R|--leave-running]}}`
