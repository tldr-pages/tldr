# putty

> SSH, Telnet, and Rlogin client for connecting to remote servers.
> Note: On Linux, the native `ssh` client is often more convenient. PuTTY is more commonly used on Windows.
> More information: <https://www.chiark.greenend.org.uk/~sgtatham/putty/>.

- Connect to a remote host via SSH:

`putty -ssh {{username}}@{{hostname_or_ip}}`

- Connect to a remote host on a specific port:

`putty -ssh {{username}}@{{hostname_or_ip}} -P {{port}}`

- Load a saved session:

`putty -load {{session_name}}`

- Connect with a private key for authentication:

`putty -ssh {{username}}@{{hostname_or_ip}} -i {{path/to/private_key.ppk}}`

- Connect via Telnet:

`putty -telnet {{hostname_or_ip}}`

- Enable X11 forwarding:

`putty -ssh {{username}}@{{hostname_or_ip}} -X`

- Set up local port forwarding:

`putty -ssh {{username}}@{{hostname_or_ip}} -L {{local_port}}:{{destination_host}}:{{destination_port}}`

- Display help:

`putty -help`
