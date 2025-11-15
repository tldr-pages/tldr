# systemctl edit

> Edit systemd unit files.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#edit%20UNIT%E2%80%A6>.

- Overlay a unit file non-destructively:

`sudo systemctl edit {{unit_file}}`

- Edit an unit file:

`sudo systemctl edit {{unit_file}} {{[-l|--full]}}`

- Create a new unit file:

`sudo systemctl edit {{unit_file}} {{[-lf|--full --force]}}`

- Overlay a user unit file:

`systemctl edit {{unit_file}} --user`
