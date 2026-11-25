# virt-qemu-run

> ابزار آزمایشی برای اجرای ماشین مجازی مهمان QEMU مستقل از `libvirtd`.
> اطلاعات بیشتر: <https://libvirt.org/manpages/virt-qemu-run.html>.

- اجرای ماشین مجازی QEMU:

`virt-qemu-run {{path/to/guest.xml}}`

- اجرای ماشین مجازی QEMU و ذخیرهٔ وضعیت در دایرکتوری مشخص:

`virt-qemu-run {{[-r|--root]}} {{path/to/directory}} {{path/to/guest.xml}}`

- اجرای ماشین مجازی QEMU و نمایش اطلاعات مفصل راه‌اندازی:

`virt-qemu-run {{[-v|--verbose]}} {{path/to/guest.xml}}`

- نمایش راهنما:

`virt-qemu-run {{[-h|--help]}}`
