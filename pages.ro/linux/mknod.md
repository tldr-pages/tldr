# mknod

> Creați fișiere speciale pentru dispozitive bloc sau caractere.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/mknod>

- Creați un dispozitiv bloc:

`sudo mknod {{path/to/device_file}} b {{major_device_number}} {{minor_device_number}}`

- Creați un dispozitiv de caractere:

`sudo mknod {{path/to/device_file}} c {{major_device_number}} {{minor_device_number}}`

- Creați un dispozitiv FIFO (coadă):

`sudo mknod {{path/to/device_file}} p`

- Creați un fișier de dispozitiv cu context implicit de securitate SELinux:

`sudo mknod -Z {{path/to/device_file}} {{type}} {{major_device_number}} {{minor_device_number}}`
