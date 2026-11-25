# grub-file

> بررسی اینکه آیا فایل از نوع تصویر قابل راه‌اندازی است.
> اطلاعات بیشتر: <https://manned.org/grub-file>.

- بررسی تصویر ARM EFI بودن فایل:

`grub-file --is-arm-efi {{path/to/file}}`

- بررسی تصویر i386 EFI بودن فایل:

`grub-file --is-i386-efi {{path/to/file}}`

- بررسی تصویر x86_64 EFI بودن فایل:

`grub-file --is-x86_64-efi {{path/to/file}}`

- بررسی تصویر ARM بودن فایل (هستهٔ لینوکس):

`grub-file --is-arm-linux {{path/to/file}}`

- بررسی تصویر x86 بودن فایل (هستهٔ لینوکس):

`grub-file --is-x86-linux {{path/to/file}}`

- بررسی تصویر x86_64 XNU بودن فایل (هستهٔ macOS):

`grub-file --is-x86_64-xnu {{path/to/file}}`
