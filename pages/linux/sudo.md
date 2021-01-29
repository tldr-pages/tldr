# sudo

> Execute a command as another user.
> More information: <https://www.sudo.ws/sudo.html>.

- Run a command with root privileges:

`sudo {{command}}`

- Repeats the last command and adds sudo at the beginning of the line:

`sudo !!`

- Open an interactive shell as root with his environment and read login-specific files (.profile, .bash_profile, ...):

`sudo --login`

- Open an interactive shell as root without his environment:

`sudo --shell`

- Open an interactive shell as a user with his environment and read login-specific files (.profile, .bash_profile, ...):

`sudo --login --user={{username}}`

- List the allowed (and forbidden) commands for the invoking user:

`sudo -l`
