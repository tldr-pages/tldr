# systemd-ask-password

> Query the user for a system password.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-ask-password.html>.

- Query a system password with a specific message:

`systemd-ask-password "{{message}}"`

- Specify an identifier for the password query:

`systemd-ask-password --id={{identifier}} "{{message}}"`

- Use a kernel keyring key name as a cache for the password:

`systemd-ask-password --keyname={{key_name}} "{{message}}"`

- Set a custom timeout for the password query:

`systemd-ask-password --timeout={{seconds}} "{{message}}"`

- Force the use of an agent system and never ask on current TTY:

`systemd-ask-password --no-tty "{{message}}"`

- Store a password in the kernel keyring without displaying it:

`systemd-ask-password --no-output --keyname={{key_name}} "{{message}}"`
