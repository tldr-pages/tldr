# ukify

> Build and sign Unified Kernel Images (UKI).
> More information: <https://www.freedesktop.org/software/systemd/man/ukify.html>.

- Build a Unified Kernel Image:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=/dev/sda1}}"`

- Build a UKI with multiple initrd files:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd1.img}} --initrd {{path/to/initrd2.img}} --cmdline "{{root=/dev/sda1}}"`

- Specify output file:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=/dev/sda1}}" --output {{uki.efi}}`

- Add microcode:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --microcode {{path/to/microcode.img}} --cmdline "{{root=/dev/sda1}}"`

- Sign the UKI for Secure Boot:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=/dev/sda1}}" --secureboot-private-key {{key.pem}} --secureboot-certificate {{cert.pem}}`

- Inspect a UKI file:

`ukify inspect {{path/to/uki.efi}}`

- Generate signing keys:

`ukify genkey --secureboot-certificate-validity {{365}}`

- Display help:

`ukify --help`
