# rdpsign

> A tool for signing Remote Desktop Protocol (RDP) files.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/rdpsign>.

- Sign an RDP file:

`rdpsign {{path\to\file.rdp}}`

- Sign an RDP file using a specific sha256 hash:

`rdpsign {{path\to\file.rdp}} /sha265 {{hash}}`

- Enable quiet output:

`rdpsign {{path\to\file.rdp}} /q`

- Display verbose warnings, messages and statuses:

`rdpsign {{path\to\file.rdp}} /v`

- Test the signing by displaying the output to `stdout` without updating the file:

`rdpsign {{path\to\file.rdp}} /l`
