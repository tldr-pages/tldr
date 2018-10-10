# rdpsign

> A tool for signing Remote Desktop Protocol (RDP) files.

- Sign an RDP file:

`rdpsign {{path/to/file.rdp}}`

- Sign an RDP file using a specific sha256 hash:

`rdpsign {{path/to/file.rdp}} /sha265 {{hash}}`

- Enable quiet output:

`rdpsign {{path/to/file.rdp}} /q`

- Display verbose warnings, messages and statuses:

`rdpsign {{path/to/file.rdp}} /v`

- Test the signing and output the result without updating the input:

`rdpsign {{path/to/file.rdp}} /l`
