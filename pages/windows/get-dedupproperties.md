# Get-DedupProperties

> Gets Data Deduplication information
> Note: This command can only be used through PowerShell.
> More Information: <https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- Get Data Deduplication information of the Drive:
`Get-DedupProperties -DriveLetter 'C'`

- Get Data Deduplication information of the Drive using the drive label:
`Get-DedupProperties -FileSystemLabel 'Label'`

- Get Data Dedpulication information of the Drive using the input object:
`Get-DedupProperties -InputObject $(Get-Volume -DriveLetter 'E')`
