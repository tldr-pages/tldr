# Get-DedupProperties

> Gets Data Deduplication information.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- Get Data Deduplication information of the drive:

`Get-DedupProperties -DriveLetter 'C'`

- Get Data Deduplication information of the drive using the drive label:

`Get-DedupProperties -FileSystemLabel 'Label'`

- Get Data Dedpulication information of the drive using the input object:

`Get-DedupProperties -InputObject $(Get-Volume -DriveLetter 'E')`
