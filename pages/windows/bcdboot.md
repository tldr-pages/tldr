# bcdboot

> Configure or repair boot files.
> More information: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- Initialize the system partition by using BCD files from the source Windows folder:

`bcdboot {{C:\Windows}}`

- Enable [v]erbose mode:

`bcdboot {{C:\Windows}} /v`

- Specify the volume letter of the [s]ystem partition:

`bcdboot {{C:\Windows}} /s {{S:}}`

- Specify a [l]ocale:

`bcdboot {{C:\Windows}} /l {{en-us}}`

- Specify a [f]irmware type while copying the boot files to a specified volume:

`bcdboot {{C:\Windows}} /s {{S:}} /f {{UEFI|BIOS|ALL}}`
