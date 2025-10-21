# gcb

> A powershell command to get content from clipboard.
> This command is an alias of `Get-Clipboard`.
> More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-clipboard>.

- Get clipboard text:

`gcb`

- Get clipboard content as specific text format:

`gcb -TextFormatType {{Text|Html|Rtf}}`

- Get raw clipboard content:

`gcb -Raw`

- Retrive an Image:

`gcb -Format Image`

- Get file paths copied in explorer:

`gcb -Format FileDropList`