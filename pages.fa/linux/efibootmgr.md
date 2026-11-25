# efibootmgr

> تغییر مدیر راه‌اندازی UEFI.
> اطلاعات بیشتر: <https://manned.org/efibootmgr>.

- فهرست کردن همهٔ گزینه‌های راه‌اندازی با شماره‌های آن‌ها:

`efibootmgr {{[-u|--unicode]}}`

- افزودن یک فایل اجرایی UEFI (مانند پوستهٔ UEFI یا تصویر یکپارچهٔ هسته) به‌عنوان گزینهٔ راه‌اندازی:

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{path\to\executable.efi}}" {{[-L|--label]}} "{{boot_entry_name}}"`

- افزودن لینوکس به‌عنوان گزینهٔ راه‌اندازی:

`sudo efibootmgr {{[-c|--create]}} {{[-d|--disk]}} {{/dev/sda}} {{[-p|--part]}} {{1}} {{[-l|--loader]}} "{{path\to\vmlinuz}}" {{[-u|--unicode]}} "{{root=UUID=partition_uuid rw loglevel=3 initrd=path\to\initramfs-linux.img}}" {{[-L|--label]}} "{{Linux}}"`

- تغییر ترتیب فعلی راه‌اندازی:

`sudo efibootmgr {{[-o|--bootorder]}} {{0002,0008,0001,001A,...}}`

- حذف یک گزینهٔ راه‌اندازی:

`sudo efibootmgr {{[-B|--delete-bootnum]}} {{[-b|--bootnum]}} {{0008}}`
