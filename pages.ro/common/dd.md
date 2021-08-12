# dd

> Conversia și copierea unui fișier.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/dd>

- Faceți o unitate USB bootabilă dintr-un fișier isohybrid (cum ar fi `archlinux-xxx.iso`) și arătați progresul:

`dd if={{file.iso}} of=/dev/{{usb_drive}} status=progress`

- Clonați o unitate pe o altă unitate cu bloc de 4MB, ignorați eroarea și arătați progresul:

`dd if=/dev/{{source_drive}} of=/dev/{{dest_drive}} bs=4M conv=noerror status=progress`

- Generați un fișier de 100 de octeți aleatoare utilizând driverul aleator kernel:

`dd if=/dev/urandom of={{random_file}} bs=100 count=1`

- Benchmark performanța de scriere a unui disc:

`dd if=/dev/zero of={{file_1GB}} bs=1024 count=1000000`

- Generați o copie de rezervă a sistemului într-un fișier IMG și arătați progresul:

`dd if=/dev/{{drive_device}} of={{path/to/file.img}} status=progress`

- Restaurați o unitate dintr-un fișier IMG și arătați progresul:

`dd if={{path/to/file.img}} of=/dev/{{drive_device}} status=progress`

- Verificați progresul unei operațiuni dd în curs de desfășurare (Rulați această comandă dintr-un alt shell):

`kill -USR1 $(pgrep ^dd)`
