# qemu-img

> Instrument pentru crearea și manipularea imaginilor HDD virtuale Emulator rapid.

- Creați o imagine de disc cu o anumită dimensiune (în gigaocteți):

`qemu-img create {{image_name.img}} {{gigabytes}}G`

- Afișați informații despre o imagine de disc:

`qemu-img info {{image_name.img}}`

- Măriți sau micșorați dimensiunea imaginii:

`qemu-img resize {{image_name.img}} {{gigabytes}}G`

- Dump starea de alocare a fiecărui sector al imaginii de disc specificate:

`qemu-img map {{image_name.img}}`

- Conversia unei imagini de disc VMware .vmdk la o imagine de disc KVM .qcow2:

`qemu-img convert -O qcow2 {{path/to/file/foo.vmdk}} {{path/to/file/foo.qcow2}}`
