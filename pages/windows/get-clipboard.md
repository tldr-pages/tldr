# Get-Clipboard

> A powershell command to get content from clipboard.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-clipboard>.

- Get clipboard text:

`Get-Clipboard`

- Get clipboard content as specific text format:

`Get-Clipboard -TextFormatType {{Text|Html|Rtf}}`

- Get raw clipboard content:

`Get-Clipboard -Raw`

- Retrieve an Image:

`Get-Clipboard -Format Image`

- Get file paths copied in explorer:

`Get-Clipboard -Format FileDropList`
