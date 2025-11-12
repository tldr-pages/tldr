# sulogin

> Log in as root during single-user mode.
> More information: <https://manned.org/sulogin>.

- Start `sulogin` on the default console:

`sudo sulogin`

- Start `sulogin` on a specific TTY device:

`sudo sulogin {{/dev/ttyX}}`

- Set a maximum timeout(in seconds) for entering the root password before continuing normal boot:

`sudo sulogin {{[-t|--timeout]}} {{timeout}}`

- Start root's shell as a login shell:

`sudo sulogin {{[-p|--login-shell]}}`

- Force a root shell without asking for a password when default methods of obtaining the password fail:

`sudo sulogin {{[-e|--force]}}`
