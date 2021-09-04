# pacman-key

> Wrapper script for GnuPG used to manage pacman’s keyring.
> More information: <https://man.archlinux.org/man/pacman-key>.

- Initialize the pacman keyring:

`sudo pacman-key --init`

- Add the default ArchLinux keys:

`sudo pacman-key --populate {{archlinux}}`

- List keys from the public keyring:

`pacman-key --list-keys`

- Add the specified keys:

`sudo pacman-key --add {{path/to/keyfile}}`

- Receive a key from a key server:

`sudo pacman-key --recv-keys "{{key_id}}"`

- Print the fingerprint of a specific key:

`pacman-key --finger "{{key_id}}"`

- Sign an imported key locally:

`sudo pacman-key --lsign-key "{{key_id}}"`

- Remove a specific key:

`sudo pacman-key {{key_id}}`
