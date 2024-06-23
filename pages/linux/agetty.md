# agetty

> Alternative `getty`: Open a `tty` port, prompt for a login name, and invoke the `/bin/login` command.
> It is normally invoked by `init`.
> Note: the baud rate is the speed of data transfer between a terminal and a device over a serial connection.
> More information: <https://manned.org/agetty>.

- Connect `stdin` to a port (relative to `/dev`) and optionally specify a baud rate (defaults to 9600):

`agetty {{tty}} {{115200}}`

- Assume `stdin` is already connected to a `tty` and set a timeout for the login:

`agetty {{-t|--timeout}} {{timeout_in_seconds}} -`

- Assume the `tty` is [8]-bit, overriding the `TERM` environment variable set by `init`:

`agetty -8 - {{term_var}}`

- Skip the login (no login) and invoke, as root, another login program instead of `/bin/login`:

`agetty {{-n|--skip-login}} {{-l|--login-program}} {{login_program}} {{tty}}`

- Do not display the pre-login (issue) file (`/etc/issue` by default) before writing the login prompt:

`agetty {{-i|--noissue}} -`

- Change the root directory and write a specific fake host into the `utmp` file:

`agetty {{-r|--chroot}} {{/path/to/root_directory}} {{-H|--host}} {{fake_host}} -`
