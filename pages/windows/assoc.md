# assoc

> Display or change associations between file extensions and file types.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/assoc>.

- List all associations between file extensions and file types:

`assoc`

- Display the associated file type for a specific extension:

`assoc {{.txt}}`

- Set the associated file type for a specific extension:

`assoc .{{txt}}={{txtfile}}`
