# systemctl isolate

> Start the specified unit with its dependencies and stop all others.
> Ignores the units which have `IgnoreOnIsolate=yes`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#isolate%20UNIT>.

- Switch to a target (assumed `.target` if no extension provided):

`systemctl isolate {{target}}`

- Switch to graphical target explicitly:

`systemctl isolate graphical.target`

- Switch to rescue (single-user) mode:

`systemctl isolate rescue.target`

- Switch to emergency mode:

`systemctl isolate emergency.target`
