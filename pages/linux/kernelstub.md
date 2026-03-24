# kernelstub

> Automatically manage Linux kernel loading on (U)EFI.
> More information: <https://github.com/isantop/kernelstub#usage>.

- Configure the current kernel with default options:

`sudo kernelstub`

- Add custom kernel options:

`sudo kernelstub {{[-o|--options]}} "{{quiet splash mitigations=off}}"`

- Run in verbose mode with `systemd-boot` configuration:

`sudo kernelstub {{[-v|--verbose]}} {{[-l|--loader]}}`

- Copy kernel only to ESP without NVRAM changes:

`sudo kernelstub {{[-m|--manage-only]}}`

- Simulation mode without changes (dry-run):

`sudo kernelstub {{[-c|--dry-run]}}`

- Specify paths manually:

`sudo kernelstub {{[-k|--kernel-path]}} /{{path/to/vmlinuz}} {{[-i|--initrd-path]}} /{{path/to/initrd.img}} {{[-e|--esp-path]}} /{{path/to/efi_partition}}`

- Show current configuration:

`sudo kernelstub {{[-p|--print-config]}}`
