# parted

> برنامهٔ تغییر پارتیشن‌ها.
> همچنین : `parted.interactive`, `cfdisk`, `partprobe`.
> اطلاعات بیشتر: <https://www.gnu.org/software/parted/manual/parted.html#Invoking-Parted>.

- فهرست کردن پارتیشن‌های همهٔ دستگاه‌های بلوکی:

`sudo parted {{[-l|--list]}}`

- ایجاد جدول پارتیشن جدید با نوع برچسب مشخص:

`sudo parted {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- ایجاد جدول پارتیشن `gpt` جدید با پارتیشن راه‌اندازی ۵۰۰ MiB و تخصیص باقی فضا به پارتیشن سیستم (`--script` پرسش‌های تعامل با کاربر را رد می‌کند):

`sudo parted {{/dev/sdX}} {{[-s|--script]}} mklabel gpt mkpart "{{boot_partition_name}}" 0% 500MiB mkpart "{{system_partition_name}}" 500MiB 100%`

- فعال کردن پرچم راه‌اندازی پارتیشن:

`sudo parted {{/dev/sdX}} set {{1}} boot on`

- شروع حالت تعاملی با دیسک مشخص انتخاب‌شده:

`sudo parted {{/dev/sdX}}`

- نمایش راهنما:

`parted {{[-h|--help]}}`
