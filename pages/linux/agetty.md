# agetty

> Alternative `getty`: Open a `tty` port, prompt for a login name, and invoke the `/bin/login` command.
> It is normally invoked by `init`.
> Note: the baud rate is the speed of data transfer between a terminal and a device over a serial connection.
> More information: <https://manned.org/agetty>.

- Connect `stdin` to a port (relative to `/dev`) and optionally specify a baud rate (defaults to 9600):

`agetty {{tty}} {{115200}}`

- Assume `stdin` is already connected to a `tty` and set a [t]imeout for the login:

`agetty {{-t|--timeout}} {{timeout_in_seconds}} -`

- Assume the `tty` is [8]-bit, overriding the `TERM` environment variable set by `init`:

`agetty -8 - {{term_var}}`

- Skip the login ([n]o login) and invoke, as root, another [l]ogin program instead of `/bin/login`:

`agetty {{-n|--skip-login}} {{-l|--login-program}} {{login_program}} {{tty}}`

- Do not display the pre-login ([i]ssue) file (`/etc/issue` by default) before writing the login prompt:

`agetty {{-i|--noissue}} -`

- Change the [r]oot directory and write a specific fake [H]ost into the `utmp` file:

`agetty {{-r|--chroot}} {{/path/to/root_directory}} {{-H|--host}} {{fake_host}} -`
