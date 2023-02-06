# partx

> A partíciós tábla elemzése és a kernel tájékoztatása. További információ: <https://man7.org/linux/man-pages/man8/partx.8.html>.

- Egy blokkeszköz vagy lemezkép partícióinak listázása:

`sudo partx --list {{path/to/device_or_disk_image}}`

- Egy adott blokkeszközön található összes partíció hozzáadása a kernelhez:

`sudo partx --add --verbose {{path/to/device_or_disk_image}}`

- A kernelben található összes partíció törlése (nem módosítja a lemezen lévő partíciókat):

`sudo partx --delete {{path/to/device_or_disk_image}}`
