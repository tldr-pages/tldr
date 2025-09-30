# pacman-key

> Wrapper script for GnuPG used to manage pacman's keyring.
> See also: `pacman`.
> More information: <https://manned.org/pacman-key>.

- Initialize the `pacman` keyring:

`sudo pacman-key --init`

- Add the default Arch Linux keys:

`sudo pacman-key --populate`

- List keys from the public keyring:

`pacman-key {{[-l|--list-keys]}}`

- Add the specified keys:

`sudo pacman-key {{[-a|--add]}} {{path/to/keyfile.gpg}}`

- Receive a key from a key server:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|name|email}}"`

- Print the fingerprint of a specific key:

`pacman-key {{[-f|--finger]}} "{{uid|name|email}}"`

- Sign an imported key locally:

`sudo pacman-key --lsign-key "{{uid|name|email}}"`

- Remove a specific key:

`sudo pacman-key {{[-d|--delete]}} "{{uid|name|email}}"`
