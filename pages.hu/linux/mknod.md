# mknod

> Blokk vagy karakteres eszköz speciális fájlok létrehozása. További információ: <https://www.gnu.org/software/coreutils/mknod>.

- Blokkeszköz létrehozása:

`sudo mknod {{path/to/device_file}} b {{major_device_number}} {{minor_device_number}}`

- Karakteres eszköz létrehozása:

`sudo mknod {{path/to/device_file}} c {{major_device_number}} {{minor_device_number}}`

- FIFO (sorban álló) eszköz létrehozása:

`sudo mknod {{path/to/device_file}} p`

- Eszközfájl létrehozása alapértelmezett SELinux biztonsági kontextussal:

`sudo mknod -Z {{path/to/device_file}} {{type}} {{major_device_number}} {{minor_device_number}}`
