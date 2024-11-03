# nxc mssql

> Pentest and exploit Microsoft SQL servers.
> More information: <https://www.netexec.wiki/mssql-protocol>.

- Search for valid credentials by trying out every combination in the specified lists of [u]sernames and [p]asswords:

`nxc mssql {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- Execute the specified SQL [q]uery on the target server:

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} --query '{{SELECT * FROM sys.databases;}}'`

- Execute the specified shell command on the target server through MSSQL:

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} -x {{whoami}}`

- Execute the specified PowerShell command on the target server through MSSQL without retrieving output:

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} -X {{whoami}} --no-output`

- Download a remote file from the target server and store it in the specified location:

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} --get-file {{C:\path\to\remote_file}} {{path/to/local_file}}`

- Upload a local file to the specified location on the target server:

`nxc mssql {{192.168.178.2}} -u {{username}} -p {{password}} --put-file {{path/to/local_file}} {{C:\path\to\remote_file}}`
