# mkinitcpio

> Generează medii ramdisk iniţiale pentru pornirea nucleului Linux pe baza presetărilor specificate.
> Mai multe informaţii: <https://man.archlinux.org/man/mkinitcpio.8>

- Efectuați o rulare uscată (imprimați ceea ce s-ar face fără a face de fapt):

`mkinitcpio`

- Generarea unui mediu ramdisk bazat pe presetarea `linux':

`mkinitcpio --preset {{linux}}`

- Generarea unui mediu ramdisk bazat pe presetarea `linux-lts`:

`mkinitcpio --preset {{linux-lts}}`

- Generează medii ramdisk bazate pe toate presetările existente (utilizate pentru a regenera toate imaginile initramfs după o modificare în `/etc/mkinitcpio.conf`):

`mkinitcpio --allpresets`

- Generarea unei imagini initramfs folosind un fişier de configurare alternativ:

`mkinitcpio --config {{path/to/mkinitcpio.conf}} --generate {{path/to/initramfs.img}}`

- Generează o imagine initramfs pentru un alt nucleu decât cel care rulează în prezent (versiunile kernel-ului instalate pot fi găsite în `/usr/lib/modules/`):

`mkinitcpio --kernel {{kernel_version}} --generate {{path/to/initramfs.img}}`

- Listează toate cârligele disponibile:

`mkinitcpio --listhooks`

- Ajutor de afișare pentru un cârlig specific:

`mkinitcpio --hookhelp {{hook_name}}`
