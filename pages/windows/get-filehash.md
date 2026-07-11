# Get-FileHash

> Calculate cryptographic checksums for a file.
> Note: This command can only be used through PowerShell.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- Calculate the SHA256 checksum for a file:

`Get-FileHash {{path\to\file}}`

- Calculate the checksum for a file using a specified algorithm:

`Get-FileHash {{path\to\file}} -Algorithm {{SHA1|SHA256|SHA384|SHA512|MD5}}`

- Calculate the checksum for a file using a deprecated algorithm (no longer available in PowerShell 6 or later):

`Get-FileHash {{path\to\file}} -Algorithm {{MACTripleDES|MD5|RIPEMD160}}`

- Check a known checksum of a file:

`(Get-FileHash {{path\to\file}} -Algorithm {{SHA1|SHA256|SHA384|SHA512|MD5}}).Hash -eq "{{known_hash}}"`
