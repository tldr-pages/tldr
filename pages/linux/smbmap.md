# smbmap

> SMB enumeration tool.
> More information: <https://github.com/ShawnDEvans/smbmap>.

- Enumerate SMB shares and permissions on a host:

`smbmap -u {{username}} -p {{password}} -H {{ip}}`

- Enumerate SMB shares and permissions on a host, specifying the domain and passing the password NTLM hash:

`smbmap -u {{username}} -p {{ntlm_hash}} -d {{domain}} -H {{ip}}`

- Enumerate SMB shares and list a single level of directories and files:

`smbmap -u {{username}} -p {{password}} -H {{ip}} -r`

- Enumerate SMB shares and recursively list a defined number of levels of directories and files:

`smbmap -u {{username}} -p {{password}} -H {{ip}} -R --depth {{3}}`

- Enumerate SMB shares and recursively list directories and files, downloading the files matching a regular expression:

`smbmap -u {{username}} -p {{password}} -H {{ip}} -R -A {{pattern}}`

- Enumerate SMB shares and recursively list directories and files, searching for file content matching a regular expression:

`smbmap -u {{username}} -p {{password}} -H {{ip}} -R -F {{pattern}}`

- Execute an OS command on a remote system:

`smbmap -u {{username}} -p {{password}} -H {{ip}} -x {{command}}`

- Upload a file on a remote system:

`smbmap -u {{username}} -p {{password}} -H {{ip}} --upload {{source}} {{destination}}`
