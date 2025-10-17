# smbmap

> Enumerate samba share drives across an entire domain.
> More information: <https://github.com/ShawnDEvans/smbmap>.

- Enumerate hosts with NULL sessions enabled and open shares:

`smbmap --host-file {{path/to/file}}`

- Display SMB shares and permissions on a [H]ost, prompting for user's password or NTLM hash:

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip}}`

- Execute a shell command on a remote system:

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip}} -x {{command}}`

- Enumerate hosts and check SMB file permissions:

`smbmap --host-file {{path/to/file}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -q`

- Connect to an ip or hostname through smb using a username and password:

`smbmap {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain}} -H {{ip_or_hostname}}`

- Locate and download files [R]ecursively up to N levels depth, searching for filename pattern (`regex`), and excluding certain shares:

`smbmap --host-file {{path/to/file}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -q -R --depth {{number}} --exclude {{sharename}} -A {{filepattern}}`

- Upload file through smb using username and password:

`smbmap {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain}} -H {{ip_or_hostname}} --upload {{path/to/file}} '{{/share_name/remote_filename}}'`

- Display SMB shares and recursively list directories and files, searching for file content matching a `regex`:

`smbmap {{[-u|--username]}} {{username}} --prompt -H {{ip}} -R -F {{pattern}}`
