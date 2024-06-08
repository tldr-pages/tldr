# Set-Volume

> Sets or changes the file system label of an existing volume.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/storage/set-volume>.

- Change the file system label of a volume identified by drive letter:

`Set-Volume -DriveLetter "D" -NewFileSystemLabel "DataVolume"`

- Change the file system label of a volume identified by the system label:

`Set-Volume -FileSystemLabel "OldLabel" -NewFileSystemLabel "NewLabel"`

- Modify the properties of a volume using a volume object:

`Set-Volume -InputObject $(Get-Volume -DriveLetter "E") -NewFileSystemLabel "Backup"`

- Specify the Data Deduplication mode for the volume:

`Set-Volume -DriveLetter "D" -DedupMode Backup`
