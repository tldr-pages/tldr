# btrfs check

> Verifica o repara un sistema de archivos btrfs.
> Más información: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- Verifica un sistema de archivos btrfs:

`sudo btrfs check {{ruta/a/la/partición}}`

- Verifica y repara un sistema de archivos btrfs (peligroso):

`sudo btrfs check --repair {{ruta/a/la/partición}}`

- Muestra el progreso de la verificación:

`sudo btrfs check --progress {{ruta/a/la/partición}}`

- Verifica la suma de comprobación de cada bloque de datos (si el sistema de archivos es bueno):

`sudo btrfs check --check-data-csum {{ruta/a/la/partición}}`

- Utiliza el superblock `n`-ésimo (`n` puede ser 0, 1 o 2):

`sudo btrfs check --super {{n}} {{ruta/a/la/partición}}`

- Reconstruye el árbol de suma de comprobación:

`sudo btrfs check --repair --init-csum-tree {{ruta/a/la/partición}}`

- Reconstruye el árbol de extensiones:

`sudo btrfs check --repair --init-extent-tree {{ruta/a/la/partición}}`
