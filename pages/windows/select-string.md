# Select-String

> Finds text in strings and files in PowerShell.
> This command can only be used through PowerShell.
> You can use `Select-String` similar to grep in UNIX or findstr.exe in Windows.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- Search for a pattern within a file:

`Select-String -Path "{{path\to\file}}" -Pattern '{{search_pattern}}'`

- Search for an exact string (disables regular expressions):

`Select-String -SimpleMatch "{{exact_string}}" {{path\to\file}}`

- Search for pattern in all `.ext` files in current dir:

`Select-String -Path "{{*.ext}}" -Pattern '{{search_pattern}}'`

- Capture the specified number of lines before and after the line that matches the pattern:

`Select-String --Context {{2,3}} "{{search_pattern}}" {{path\to\file}}`

- Search stdin for lines that do not match a pattern:

`Get-Content {{path\to\file}} | Select-String --NotMatch "{{search_pattern}}"`
