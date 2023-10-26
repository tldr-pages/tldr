# wget

> In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `wget` program (<https://www.gnu.org/software/wget>) is not properly installed.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Check whether `wget` is properly installed by printing its version number. If this command evaluates into an error, PowerShell may have substituted this command with `Invoke-WebRequest`:

`wget --version`

- View documentation for the original `wget` command:

`tldr wget -p common`

- View documentation for the original `wget` command in older versions of `tldr` command-line client:

`tldr wget -o common`

- View documentation for PowerShell's `Invoke-WebRequest` command:

`tldr invoke-webrequest`
