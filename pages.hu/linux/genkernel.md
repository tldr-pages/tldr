# genkernel

> Gentoo Linux segédprogram a kernelek fordításához és telepítéséhez. További információ: <https://wiki.gentoo.org/wiki/Genkernel>.

- Általános rendszermag automatikus fordítása és telepítése:

`sudo genkernel all`

- Csak a bzImage|initramfs|kernel|ramdisk összeállítása és telepítése:

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- Alkalmazza a kernel konfigurációjának módosításait a fordítás és telepítés előtt:

`sudo genkernel --menuconfig all`

- Egyéni nevű kernel generálása:

`sudo genkernel --kernname={{custom_name}} all`

- Az alapértelmezett könyvtáron kívüli kernelforrás használata `/usr/src/linux`:

`sudo genkernel --kerneldir={{path/to/directory}} all`
