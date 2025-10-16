# ventoy

> A tool to create bootable USB drives using ISO files on Windows systems.
> More information: <https://www.ventoy.net/en/doc_windows_cli.html>.

- Install Ventoy to drive D: with default settings (MBR, Secure Boot enabled):

`Ventoy2Disk.exe VTOYCLI /I /Drive:D:`

- Install Ventoy with GPT partition style and disable Secure Boot:

`Ventoy2Disk.exe VTOYCLI /I /Drive:D: /GPT /NOSB`

- Install Ventoy and reserve 4GB space at the end of the disk:

`Ventoy2Disk.exe VTOYCLI /I /Drive:D: /R:4096`

- Install Ventoy using physical drive number 1 with NTFS filesystem:

`Ventoy2Disk.exe VTOYCLI /I /PhyDrive:1 /FS:NTFS`

- Install Ventoy without USB type checking (for internal drives):

`Ventoy2Disk.exe VTOYCLI /I /Drive:D: /NOUSBCheck`

- Update Ventoy on drive D: while keeping current settings:

`Ventoy2Disk.exe VTOYCLI /U /Drive:D:`

- Perform non-destructive installation (preserve existing data):

`Ventoy2Disk.exe VTOYCLI /I /Drive:D: /NonDest`

- Install Ventoy with all options: GPT, no Secure Boot, 2GB reserved, NTFS, no USB check:

`Ventoy2Disk.exe VTOYCLI /I /Drive:D: /GPT /NOSB /R:2048 /FS:NTFS /NOUSBCheck`
