# crackmapexec

> Network penetration testing tool for assessing the security of large Active Directory networks.
> See also: `nmap`, `smbclient`, `enum4linux`.
> More information: <https://github.com/byt3bl33d3r/CrackMapExec>.

- Enumerate SMB shares on a host or subnet:

`crackmapexec smb {{ip_or_cidr}} --shares`

- Authenticate to SMB with a username and password:

`crackmapexec smb {{ip_or_hostname}} -u {{username}} -p {{password}}`

- Authenticate using an NTLM hash (Pass-the-Hash):

`crackmapexec smb {{ip_or_hostname}} -u {{username}} -H {{nt_hash}}`

- Enumerate logged-on users:

`crackmapexec smb {{ip_or_hostname}} -u {{username}} -p {{password}} --loggedon-users`

- Execute a command on a remote host:

`crackmapexec smb {{ip_or_hostname}} -u {{username}} -p {{password}} -x "{{command}}"`

- Dump SAM hashes from a remote host:

`crackmapexec smb {{ip_or_hostname}} -u {{username}} -p {{password}} --sam`

- Spray a password across multiple hosts:

`crackmapexec smb {{path/to/hosts.txt}} -u {{username}} -p {{password}}`

- Enumerate via WinRM protocol:

`crackmapexec winrm {{ip_or_hostname}} -u {{username}} -p {{password}}`
