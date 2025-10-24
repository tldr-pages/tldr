# Get-Clipboard

> A powershell command to get content from clipboard.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-clipboard>.

- Get clipboard text:

`{{[gcb|Get-Clipboard]}}`

- Get clipboard content as specific text format:

`{{[gcb|Get-Clipboard]}} -TextFormatType {{Text|Html|Rtf}}`

- Get raw clipboard content:

`{{[gcb|Get-Clipboard]}} -Raw`

- Retrieve an Image:

`{{[gcb|Get-Clipboard]}} -Format Image`

- Get file paths copied in explorer:

`{{[gcb|Get-Clipboard]}} -Format FileDropList`
