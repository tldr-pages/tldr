# xkbcli

> Interact with X Keyboard keymaps.
> More information: <https://manned.org/xkbcli>.

- Display how to type a key and if it needs modifiers (Note: Does not support compose sequences):

`xkbcli how-to-type {{A|0x0041}}`

- Bring up an interactive window that captures keypresses:

`xkbcli interactive`

- Compile a list of available compose sequences:

`xkbcli compile-compose`
