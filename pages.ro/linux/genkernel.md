# genkernel

> Utilitarul Gentoo Linux pentru compilarea şi instalarea kernelurilor.
> Mai multe informaţii: <https://wiki.gentoo.org/wiki/Genkernel>

- compilați și instalați automat un nucleu generic:

`sudo genkernel all`

- Construiește și instalează bzimage|Initramfs|Kernel|RamDisk numai:

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- Aplicați modificări la configurația kernel-ului înainte de compilare și instalare:

`sudo genkernel --menuconfig all`

- Generează un kernel cu un nume personalizat:

`sudo genkernel --kernname={{custom_name}} all`

- Utilizați o sursă de kernel în afara directorului implicit `/usr/src/linux`:

`sudo genkernel --kerneldir={{path/to/directory}} all`
