# grub-probe

> بررسی اطلاعات دستگاه برای مسیر یا دستگاه مشخص.
> اطلاعات بیشتر: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dprobe.html>.

- دریافت ماژول سیستم فایل GRUB برای یک مسیر:

`sudo grub-probe {{[-t|--target]}} fs {{/boot/grub}}`

- دریافت دستگاه سیستمی حاوی یک مسیر:

`sudo grub-probe {{[-t|--target]}} device {{/boot/grub}}`

- دریافت نام دیسک GRUB برای دستگاه سیستمی:

`sudo grub-probe {{[-t|--target]}} drive {{/dev/sdX}} {{[-d|--device]}}`

- دریافت UUID سیستم فایل:

`sudo grub-probe {{[-t|--target]}} fs_uuid {{/boot/grub}}`

- دریافت برچسب سیستم فایل:

`sudo grub-probe {{[-t|--target]}} fs_label {{/boot/grub}}`

- دریافت کد نوع پارتیشن MBR (دو رقم شانزده‌شانزدهی):

`sudo grub-probe {{[-t|--target]}} msdos_parttype {{/dev/sdX}}`

- بررسی با نگاشت دستگاه دلخواه:

`sudo grub-probe {{[-t|--target]}} drive {{/boot/grub}} {{[-m|--device-map]}} {{path/to/custom_device.map}}`
