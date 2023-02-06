# qemu-img

> Eszköz a Quick Emulator Virtual HDD kép létrehozásához és manipulálásához. További információ: <https://qemu.readthedocs.io/en/latest/tools/qemu-img.html>.

- Lemezkép létrehozása egy adott méretű (gigabájtban megadott) lemezről:

`qemu-img create {{image_name.img}} {{gigabytes}}G`

- A lemezképre vonatkozó információk megjelenítése:

`qemu-img info {{image_name.img}}`

- A lemezkép méretének növelése vagy csökkentése:

`qemu-img resize {{image_name.img}} {{gigabytes}}G`

- A megadott lemezkép minden szektorának kiosztási állapotának kiürítése:

`qemu-img map {{image_name.img}}`

- VMware .vmdk lemezkép átalakítása KVM .qcow2 lemezképpé:

`qemu-img convert -f {{vmdk}} -O {{qcow2}} {{path/to/file/foo.vmdk}} {{path/to/file/foo.qcow2}}`
