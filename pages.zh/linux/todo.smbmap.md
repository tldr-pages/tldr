# smbmap

> SMB enumeration tool.
> More information: <https://github.com/ShawnDEvans/smbmap>.

- Display SMB shares and permissions on a host, prompting for user's password or NTLM hash:

`smbmap -u {{username}} --prompt -H {{ip}}`

- Display SMB shares and permissions on a host, specifying the domain and passing the password NTLM hash:

`smbmap -u {{username}} --prompt -d {{domain}} -H {{ip}}`

- Display SMB shares and list a single level of directories and files:

`smbmap -u {{username}} --prompt -H {{ip}} -r`

- Display SMB shares and recursively list a defined number of levels of directories and files:

`smbmap -u {{username}} --prompt -H {{ip}} -R --depth {{3}}`

- Display SMB shares and recursively list directories and files, downloading the files matching a regular expression:

`smbmap -u {{username}} --prompt -H {{ip}} -R -A {{pattern}}`

- Display SMB shares and recursively list directories and files, searching for file content matching a regular expression:

`smbmap -u {{username}} --prompt -H {{ip}} -R -F {{pattern}}`

- Execute a shell command on a remote system:

`smbmap -u {{username}} --prompt -H {{ip}} -x {{command}}`

- Upload a file to a remote system:

`smbmap -u {{username}} --prompt -H {{ip}} --upload {{source}} {{destination}}`
