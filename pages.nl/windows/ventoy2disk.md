# Ventoy2Disk

> Een tool om opstartbare USB-schijven te maken met ISO-bestanden op Windows-systemen.
> Meer informatie: <https://www.ventoy.net/en/doc_windows_cli.html>.

- Installeer Ventoy op schijf D: met standaardinstellingen (MBR, Secure Boot ingeschakeld):

`Ventoy2Disk VTOYCLI /I /Drive:D:`

- Installeer Ventoy met GPT-partitiestijl en schakel Secure Boot uit:

`Ventoy2Disk VTOYCLI /I /Drive:D: /GPT /NOSB`

- Installeer Ventoy en reserveer 4GB ruimte aan het einde van de schijf:

`Ventoy2Disk VTOYCLI /I /Drive:D: /R:4096`

- Installeer Ventoy met fysiek schijfnummer 1 en het NTFS-bestandssysteem:

`Ventoy2Disk VTOYCLI /I /PhyDrive:1 /FS:NTFS`

- Installeer Ventoy zonder controle op het USB-type (voor interne schijven):

`Ventoy2Disk VTOYCLI /I /Drive:D: /NOUSBCheck`

- Update Ventoy op schijf D: met behoud van de huidige instellingen:

`Ventoy2Disk VTOYCLI /U /Drive:D:`

- Voer een niet-destructieve installatie uit (behoud bestaande gegevens):

`Ventoy2Disk VTOYCLI /I /Drive:D: /NonDest`

- Installeer Ventoy met alle opties: GPT, geen Secure Boot, 2GB gereserveerd, NTFS, geen USB-controle:

`Ventoy2Disk VTOYCLI /I /Drive:D: /GPT /NOSB /R:2048 /FS:NTFS /NOUSBCheck`
