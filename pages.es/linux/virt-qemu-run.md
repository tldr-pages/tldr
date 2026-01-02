# virt-qemu-run

> Herramienta experimental para ejecutar una Guest VM QEMU independiente de `libvirtd`.
> Más información: <https://libvirt.org/manpages/virt-qemu-run.html>.

- Ejecuta una máquina virtual QEMU:

`virt-qemu-run {{ruta/a/guest.xml}}`

- Ejecuta una máquina virtual QEMU y almacena el estado en un directorio específico:

`virt-qemu-run --root={{ruta/a/directorio}} {{ruta/a/guest.xml}}`

- Ejecuta una máquina virtual QEMU y muestra información detallada sobre el inicio:

`virt-qemu-run --verbose {{ruta/a/guest.xml}}`

- Muestra ayuda:

`virt-qemu-run --help`
