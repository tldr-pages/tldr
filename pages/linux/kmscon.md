# kmscon

> Use the framebuffer instead of text mode to draw a terminal in a TTY.
> More information: <https://manned.org/kmscon>.

- Start `kmscon` on the first available TTY:

`sudo kmscon`

- Start `kmscon` in a specific TTY:

`sudo kmscon --vt {{/dev/ttyX|ttyX|X}}`

- Enable mouse support:

`sudo kmscon --mouse`

- Specify the command to use for login:

`sudo kmscon {{[-l|--login]}} {{command}}`
