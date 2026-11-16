# Ventoy2Disk

> Una herramienta para crear unidades USB de arranque a partir de archivos ISO en sistemas Windows.
> Más información: <https://www.ventoy.net/en/doc_windows_cli.html>.

- Instala Ventoy en la unidad D: con la configuración predeterminada (MBR, arranque seguro activado):

`Ventoy2Disk VTOYCLI /I /Drive:D:`

- Instala Ventoy con el estilo de partición GPT y desactiva el arranque seguro:

`Ventoy2Disk VTOYCLI /I /Drive:D: /GPT /NOSB`

- Instala Ventoy y reserva 4 GB de espacio al final del disco:

`Ventoy2Disk VTOYCLI /I /Drive:D: /R:4096`

- Instala Ventoy utilizando la unidad física número 1 con el sistema de archivos NTFS:

`Ventoy2Disk VTOYCLI /I /PhyDrive:1 /FS:NTFS`

- Instala Ventoy sin comprobación del tipo de USB (para unidades internas):

`Ventoy2Disk VTOYCLI /I /Drive:D: /NOUSBCheck`

- Actualiza Ventoy en la unidad D: conservando la configuración actual:

`Ventoy2Disk VTOYCLI /U /Drive:D:`

- Realiza una instalación no destructiva (conserva los datos existentes):

`Ventoy2Disk VTOYCLI /I /Drive:D: /NonDest`

- Instala Ventoy con todas las opciones: GPT, sin arranque seguro, 2 GB reservados, NTFS, sin comprobación de USB:

`Ventoy2Disk VTOYCLI /I /Drive:D: /GPT /NOSB /R:2048 /FS:NTFS /NOUSBCheck`
