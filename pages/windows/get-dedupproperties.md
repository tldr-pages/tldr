# Get-DedupProperties

> Gets Data Deduplication information
> This command can only be used through Powershell.
> More Information: <https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- Get Data Deduplication information of the Drive:
`Get-DedupProperties -DriveLetter 'C'`

- Get Data Deduplication information of the Drive using the drive label:
`Get-DedupProperties -FileSystemLabel 'Label'`

- Get Data Dedpulication information of the Drive using the input object:
`$Volume = Get-Volume -DriveLetter 'E'`
`Get-DedupProperties -InputObject $Volume`
