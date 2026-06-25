# ntfs-read.py

> Un explorador NTFS de solo lectura para acceder y extraer archivos de volúmenes NTFS.
> Forma parte del paquete Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Abre un volumen NTFS para explorarlo (por ejemplo, `C:\.\\` o `/dev/disk1s1`):

`ntfs-read.py {{volumen}}`

- Extrae un archivo específico de un volumen NTFS (por ejemplo, `\windows\system32\config\sam`):

`ntfs-read.py -extract {{\windows\system32\config\sam}} {{volumen}}`

- Habilita la salida de depuración:

`ntfs-read.py -debug {{volumen}}`

- Muestra la ayuda:

`ntfs-read.py --help`
