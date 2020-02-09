# enum4linux

> Tool for enumerating Windows and Samba information from remote systems.
> It attempts to offer similar functionality to enum.exe formerly available from www.bindview.com.

- Try to enumerate using all methods:

`enum4linux -a {{remote_host}}`

- Enumerate using given login credentials:

`enum4liux -u {{user_name}} -p {{password}} {{remote_host}}`

- List usernames from a given host:

`enum4liux -U {{remote_host}}`

- List shares:

`enum4liux -S {{remote_host}}`

- Get OS information:

`enum4liux -o {{remote_host}}`
