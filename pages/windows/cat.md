# curl

> In PowerShell, this command may be an alias of `Get-Content` when the original `cat` program (part of `coreutils`) is not properly installed.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- View documentation for the original `cat` command:

`tldr cat {{[-p|--platform]}} common`

- View documentation for PowerShell's `Get-Content` command:

`tldr get-content`

- Check whether `cat` is properly installed by printing its version number. If this command evaluates into an error, PowerShell may have substituted this command with `Get-Content`:

`cat --version`
