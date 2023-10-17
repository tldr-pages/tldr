# bcdboot

> A system utility to configure or repair boot files.
> More information: <https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- Initialize the system partition by using BCD files from the source Windows folder:

`bcdboot {{C:\Windows}}`

- Enable verbose mode:

`bcdboot {{C:\Windows}} /v`

- Specify the volume letter of the system partition:

`bcdboot {{C:\Windows}} /s {{S:}}`

- Specify a locale:

`bcdboot {{C:\Windows}} /l {{en-us}}`

- Specify a firmware type while copying the boot files to a specified volume:

`bcdboot {{C:\Windows}} /s {{S:}} /f {{UEFI|BIOS|ALL}}`
