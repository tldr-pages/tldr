# csrutil

> Manage the System Integrity Protection configuration.
> More information: <https://ss64.com/osx/csrutil.html>.

- Display the System Integrity Protection status:

`csrutil status`

- Disable the System Integrity Protection:

`csrutil disable`

- Enable the System Integrity Protection:

`csrutil enable`

- Display the list of allowed NetBoot sources:

`csrutil netboot list`

- Add an IPv4 address to the list of allowed NetBoot sources:

`csrutil netboot add {{ip}}`

- Reset the System Integrity Protection status and clear the NetBoot list:

`csrutil clear`
