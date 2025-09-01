# rbw

> Unofficial Bitwarden-compatible password manager.
> More information: <https://github.com/doy/rbw#configuration>.

- Log in to the vault:

`rbw login`

- Unlock the vault:

`rbw unlock`

- List all items in the vault:

`rbw list`

- Get a password for an entry:

`rbw get "{{entry_name}}"`

- Get a username for an entry:

`rbw get {{[-f|--field]}} username "{{entry_name}}"`

- Copy a password to the clipboard:

`rbw get {{[-c|--clipboard]}} "{{entry_name}}"`

- Generate a new password with the specified number of characters:

`rbw generate {{password_length}}`

- Lock the vault:

`rbw lock`
