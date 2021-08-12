# partx

> Parsați o tabelă de partiții și spuneți kernel-ului despre aceasta.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/partx.8.html>

- Listați partițiile pe un dispozitiv bloc sau o imagine de disc:

`sudo partx --list {{path/to/device_or_disk_image}}`

- Adăugați toate partițiile găsite într-un anumit dispozitiv bloc la kernel:

`sudo partx --add --verbose {{path/to/device_or_disk_image}}`

- Ștergeți toate partițiile găsite din kernel (nu modifică partițiile de pe disc):

`sudo partx --delete {{path/to/device_or_disk_image}}`
