# mokutil

> Configure Secure Boot Machine Owner Keys (MOK).
> Some operations, such as enabling and disabling Secure Boot or enrolling keys require a reboot.
> More information: <https://manned.org/mokutil>.

- Show if Secure Boot is enabled:

`mokutil --sb-state`

- Enable Secure Boot:

`mokutil --enable-validation`

- Disable Secure Boot:

`mokutil --disable-validation`

- List enrolled keys:

`mokutil {{[-l|--list-enrolled]}}`

- Enroll a new key:

`mokutil {{[-i|--import]}} {{path/to/key.der}}`

- List the keys to be enrolled:

`mokutil {{[-N|--list-new]}}`

- Set shim verbosity:

`mokutil --set-verbosity true`
