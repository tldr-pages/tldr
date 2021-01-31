# sudo

> Executes a single command as the superuser or another user.
> More information: <https://www.sudo.ws/sudo.html>.

- Run a command as the superuser:

`sudo {{less /var/log/syslog}}`

- Edit a file as the superuser with your default editor:

`sudo --edit {{/etc/fstab}}`

- Run a command as another user and/or group:

`sudo --user={{user}} --group={{group}} {{id -a}}`

- Repeat the last command prefixed with `sudo` (only in `bash`, `zsh`, etc.):

`sudo !!`

- Launch the default shell with superuser privileges and run login-specific files (`.profile`, `.bash_profile`, etc.):

`sudo --login`

- Launch the default shell with superuser privileges without changing the environment:

`sudo --shell`

- Launch the default shell as the specified user, loading the user's environment and reading login-specific files (`.profile`, `.bash_profile`, etc.):

`sudo --login --user={{user}}`

- List the allowed (and forbidden) commands for the invoking user:

`sudo --list`
