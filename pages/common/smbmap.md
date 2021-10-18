# Smbmap

> Allows users to enumerate samba share drives across an entire domain.
> More information: <https://github.com/ShawnDEvans/smbmap>.

- Enumerate hosts with NULL sessions enabled and open shares:

`smbmap --host-file {{path/to/file}}`

- Enumerate hosts and check SMB file permissions:

`smbmap --host-file {{path/to/file}} -u {{username}} -p {{password}} -q`

- Connect to an ip or hostname through smb using username and password:

`smbmap -u {{username}} -p {{password}} -d {{domain}} -H {{ip_or_hostname}}`

- Locate and download files recursively according to pattern excluding certain shares:

`smbmap --host-file {{path/to/file}} -u {{username}} -p {{password}} -q -R --depth {{number}} --exclude {{SHARE$}} -A {{filepattern}}`

- Upload file through smb using username and password:

`smbmap -u {{username}} -p {{password}} -d {{domain}} -H {{ip_or_hostname}} --upload {{path/to/file}} '{{/smbshare/filename}}'`
