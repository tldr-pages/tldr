# kernelstub

> مدیریت خودکار بارگذاری هستهٔ لینوکس در (U)EFI.
> اطلاعات بیشتر: <https://github.com/isantop/kernelstub#usage>.

- پیکربندی هستهٔ فعلی با گزینه‌های پیش‌فرض:

`sudo kernelstub`

- افزودن گزینه‌های دلخواه هسته:

`sudo kernelstub {{[-o|--options]}} "{{quiet splash mitigations=off}}"`

- اجرا در حالت مفصل با پیکربندی `systemd-boot`:

`sudo kernelstub {{[-v|--verbose]}} {{[-l|--loader]}}`

- کپی فقط هسته در ESP بدون تغییر NVRAM:

`sudo kernelstub {{[-m|--manage-only]}}`

- شبیه‌سازی عملیات بدون ایجاد تغییر:

`sudo kernelstub {{[-c|--dry-run]}}`

- تعیین دستی مسیرها:

`sudo kernelstub {{[-k|--kernel-path]}} /{{path/to/vmlinuz}} {{[-i|--initrd-path]}} /{{path/to/initrd.img}} {{[-e|--esp-path]}} /{{path/to/efi_partition}}`

- نمایش پیکربندی فعلی:

`sudo kernelstub {{[-p|--print-config]}}`
