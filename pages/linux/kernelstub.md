# kernelstub

> Automatically manages Linux kernel loading on (U)EFI.
> More information: <https://github.com/isantop/kernelstub>.

- Configure current kernel with default options:

`sudo kernelstub`

- Add custom kernel options:

`sudo kernelstub {{[-o|--options]}} "{{quiet splash mitigations=off}}"`

- Verbose mode with systemd-boot configuration:

`sudo kernelstub {{[-v|--verbose]}} {{[-l|--loader]}}`

- Copy kernel only to ESP without NVRAM changes:

`sudo kernelstub -m`

- Simulation mode without changes (dry-run):

`sudo kernelstub -c`

- Specify paths manually:

`sudo kernelstub -k "{{/boot/vmlinuz}}" -i "{{/boot/initrd.img}}" -e "{{/boot/efi}}"`

- Show current configuration:

`sudo kernelstub -p`
