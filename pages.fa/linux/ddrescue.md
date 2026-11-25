# ddrescue

> ابزار بازیابی داده که داده‌ها را از دستگاه‌های بلوکی آسیب‌دیده می‌خواند.
> اطلاعات بیشتر: <https://www.gnu.org/software/ddrescue/manual/ddrescue_manual.html#Invoking-ddrescue>.

- گرفتن تصویر از یک دستگاه:

`sudo ddrescue {{/dev/sdX}} {{path/to/image.img}}`

- گرفتن تصویر از یک دستگاه و ایجاد فایل گزارش:

`sudo ddrescue {{/dev/sdX}} {{path/to/image.img}} {{path/to/log.txt}}`

- رونوشت‌گیری از دیسک A به دیسک B و ایجاد فایل گزارش:

`sudo ddrescue {{[-f|--force]}} {{[-n|--no-scrape]}} {{/dev/sdX}} {{/dev/sdY}} {{path/to/log.txt}}`
