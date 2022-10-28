# psexec

> Execute a command-line process on a remote machine.
> This is an advanced command and it might potentially be dangerous.
> More information: <https://learn.microsoft.com/en-us/sysinternals/downloads/psexec>.

- Execute a command using `cmd` in a remote shell:

`psexec \\{{remote_host}} cmd`

- Execute a command on a remote host (pre-authenticated):

`psexec \\{{remote_host}} -u {{user_name}} -p {{password}}`

- Execute a command remotely and output the result to a file:

`psexec \\{{remote_host}} cmd /c {{command}} -an ^>{{path/to/file.txt}}`

- Execute a program to interact with users:

`psexec \\{{remote_host}} -d -i {{program_name}}`

- Display the IP configuration of the remote host:

`psexec \\{{remote_host}} ipconfig /all`
