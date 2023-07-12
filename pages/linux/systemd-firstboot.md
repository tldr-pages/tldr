# systemd-firstboot

> Initialize basic system settings on or before the first boot-up of a system.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-firstboot.html>.

- Set the root directory for the basic system settings initialization:

`sudo systemd-firstboot --root={{root_directory_path}}`

- Set the system locale:

`sudo systemd-firstboot --locale={{locale}}`

- Set the system keyboard layout:

`sudo systemd-firstboot --keymap={{keymap}}`

- Set the system time zone:

`sudo systemd-firstboot --timezone={{timezone}}`

- Set the system hostname:

`sudo systemd-firstboot --hostname={{hostname}}`

- Set the system's machine ID to a random ID:

`sudo systemd-firstboot --setup-machine-id`

- Set the root user's password:

`sudo systemd-firstboot --root-password={{password}}`

- Set the shell of the system's root user:

`sudo systemd-firstboot --root-shell={{shell}}`

- Prompt the user interactively for a specific basic setting:

`sudo systemd-firstboot --prompt={{setting}}`

- Force writing configuration even if the relevant files already exist:

`sudo systemd-firstboot --force`

- Remove all existing files that are configured by systemd-firstboot:

`sudo systemd-firstboot --reset`

- Remove the password of the system's root user:

`sudo systemd-firstboot --delete-root-password`

- Disable the brief welcome text:

`sudo systemd-firstboot --welcome=false`
