# ukify

> Build and sign Unified Kernel Images (UKIs).
> More information: <https://www.freedesktop.org/software/systemd/man/ukify.html>.

- Build a Unified Kernel Image:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=/dev/sdXY}}"`

- Build a UKI with multiple initrd files:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd1.img}} --initrd {{path/to/initrd2.img}} --cmdline "{{root=/dev/sdXY}}"`

- Specify output file:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=/dev/sdXY}}" --output {{path/to/output.efi}}`

- Add microcode:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --microcode {{path/to/microcode.img}} --cmdline "{{root=/dev/sdXY}}"`

- Sign the UKI for Secure Boot:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=/dev/sdXY}}" --secureboot-private-key {{path/to/private_key.pem}} --secureboot-certificate {{path/to/certificate.pem}}`

- Inspect a UKI file:

`ukify inspect {{path/to/uki.efi}}`

- Generate signing keys:

`ukify genkey --secureboot-certificate-validity {{365}}`

- Display help:

`ukify {{[-h|--help]}}`
