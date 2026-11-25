# ukify

> ساخت و امضای تصاویر یکپارچهٔ هسته (UKI).
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/ukify.html>.

- ساخت تصویر یکپارچهٔ هسته:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=UUID=xxxx}}"`

- ساخت UKI با چند فایل initrd:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd1.img}} --initrd {{path/to/initrd2.img}} --cmdline "{{root=UUID=xxxx}}"`

- ساخت UKI با تعیین نام فایل خروجی:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=UUID=xxxx}}" --output {{path/to/output.efi}}`

- ساخت UKI شامل ریزکد CPU:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --microcode {{path/to/microcode.img}} --cmdline "{{root=UUID=xxxx}}"`

- امضای UKI برای Secure Boot:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=UUID=xxxx}}" --secureboot-private-key {{path/to/private_key.pem}} --secureboot-certificate {{path/to/certificate.pem}}`

- بررسی فایل UKI:

`ukify inspect {{path/to/uki.efi}}`

- تولید کلیدهای امضا:

`ukify genkey --secureboot-certificate-validity {{365}}`

- نمایش راهنما:

`ukify {{[-h|--help]}}`
