# systemctl set-default

> Symlink the `default.target` alias to the given target unit.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#set-default%20TARGET>.

- Set `systemd`'s default boot mode:

`systemctl set-default {{target_name.target}}`

- Set `systemd` to boot to GUI mode by default:

`systemctl set-default graphical.target`

- Set `systemd` to boot to CLI mode by default:

`systemctl set-default multi-user.target`
