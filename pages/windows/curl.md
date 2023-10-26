# curl

> In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `curl` program (<https://curl.se>) is not properly installed.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Check whether `curl` is properly installed by printing its version number. If this command evaluates into an error, PowerShell may have substituted this command with `Invoke-WebRequest`:

`curl --version`

- View documentation for the original `curl` command:

`tldr curl -p common`

- View documentation for the original `curl` command in older versions of `tldr` command-line client:

`tldr curl -o common`

- View documentation for PowerShell's `Invoke-WebRequest` command:

`tldr invoke-webrequest`
