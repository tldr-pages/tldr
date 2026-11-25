# lsinitrd

> نمایش محتویات تصویر initramfs.
> همچنین : `dracut`.
> اطلاعات بیشتر: <https://github.com/dracutdevs/dracut/blob/master/man/lsinitrd.1.asc>.

- نمایش محتویات تصویر initramfs هستهٔ فعلی:

`lsinitrd`

- نمایش محتویات تصویر initramfs هستهٔ مشخص:

`lsinitrd {{[-k|--kver]}} {{kernel_version}}`

- نمایش محتویات تصویر initramfs مشخص:

`lsinitrd {{path/to/initramfs.img}}`

- فهرست کردن ماژول‌های موجود در تصویر initramfs:

`lsinitrd {{[-m|--mod]}}`

- استخراج initramfs در دایرکتوری فعلی:

`lsinitrd --unpack`
