# Clear-RecycleBin

> Clear items from the Recycle Bin.
> This command can only be used through PowerShell versions 5.1 and below, or 7.1 and above.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.

- Clear and delete all items inside the Recycle Bin:

`Clear-RecycleBin`

- Clear the Recycle Bin for a specific drive:

`Clear-RecycleBin -DriveLetter {{C}}`

- Clear the Recycle Bin without further confirmation:

`Clear-RecycleBin -Force`
