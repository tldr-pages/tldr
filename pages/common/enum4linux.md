# enum4linux

> Enumerate information from Windows and Samba systems over SMB.
> See also: `smbclient`, `rpcclient`, `nmap`.
> More information: <https://github.com/CiscoCXSecurity/enum4linux>.

- Perform all simple enumeration checks against a host:

`enum4linux -a {{ip_or_hostname}}`

- Enumerate users on a host:

`enum4linux -U {{ip_or_hostname}}`

- Enumerate shares on a host:

`enum4linux -S {{ip_or_hostname}}`

- Enumerate groups and group members:

`enum4linux -G {{ip_or_hostname}}`

- Retrieve the password policy:

`enum4linux -P {{ip_or_hostname}}`

- Retrieve OS information:

`enum4linux -o {{ip_or_hostname}}`

- Enumerate with specific credentials:

`enum4linux -u {{username}} -p {{password}} {{ip_or_hostname}}`

- Suppress error messages and only show results:

`enum4linux -s {{path/to/shares.txt}} {{ip_or_hostname}}`
