# mokutil

> Configure Secure Boot Machine Owner Keys (MOK).
> Some operations, such as enabling and disabling Secure Boot or enrolling keys require a reboot.
> More information: <https://github.com/lcp/mokutil>.

- Show if Secure Boot is enabled:

`mokutil --sb-state`

- Enable Secure Boot:

`mokutil --enable-validation`

- Disable Secure Boot:

`mokutil --disable-validation`

- List enrolled keys:

`mokutil --list-enrolled`

- Enroll a new key:

`mokutil --import {{path/to/key.der}}`

- List the keys to be enrolled:

`mokutil --list-new`

- Set shim verbosity:

`mokutil --set-verbosity true`
