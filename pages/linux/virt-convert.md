# virt-convert

> Convert VMX / OVF to native libvirt guests.
> See also: `qemu-img`.
> More information: <https://manned.org/virt-convert>.

- Convert an OVA archive:

`virt-convert {{path/to/vm.ova}}`

- Convert an extracted virtual machine containing .vmx and .vmdk files to qcow2 format:

`virt-convert {{path/to/directory}} {{[-D|--disk-format]}} qcow2`

- Copy disk images to a destination directory without converting their formats:

`virt-convert {{path/to/vm.vmx}} {{[-D|--disk-format]}} none --destination {{/tmp}}`

- Preview the generated libvirt XML without performing the conversion:

`virt-convert {{path/to/vm.vmx}} --print-xml`
