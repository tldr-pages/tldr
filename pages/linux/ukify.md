# ukify

> Build and sign Unified Kernel Images (UKIs).
> More information: <https://www.freedesktop.org/software/systemd/man/latest/ukify.html>.

- Build a Unified Kernel Image:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=UUID=xxxx}}"`

- Build a UKI with multiple initrd files:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd1.img}} --initrd {{path/to/initrd2.img}} --cmdline "{{root=UUID=xxxx}}"`

- Build a UKI, specifying the output filename:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=UUID=xxxx}}" --output {{path/to/output.efi}}`

- Build a UKI including CPU microcode:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --microcode {{path/to/microcode.img}} --cmdline "{{root=UUID=xxxx}}"`

- Sign the UKI for Secure Boot:

`ukify build --linux {{path/to/vmlinuz}} --initrd {{path/to/initrd.img}} --cmdline "{{root=UUID=xxxx}}" --secureboot-private-key {{path/to/private_key.pem}} --secureboot-certificate {{path/to/certificate.pem}}`

- Inspect a UKI file:

`ukify inspect {{path/to/uki.efi}}`

- Generate signing keys:

`ukify genkey --secureboot-certificate-validity {{365}}`

- Display help:

`ukify {{[-h|--help]}}`
