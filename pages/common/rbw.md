# rbw

> Unofficial Bitwarden-compatible CLI password manager, written in Rust.
> More information: <https://github.com/doy/rbw>.

- Login and unlock the vault:

`rbw login`
`rbw unlock`

- List all items in the vault:

`rbw list`

- Get a password for an entry:

`rbw get {{"entry_name"}}`

- Get a username for an entry:

`rbw get {{[-f|--field]}} username {{"entry_name"}}`

- Copy a password to the clipboard:

`rbw get {{[-c|--clipboard]}} {{"entry_name"}}`

- Generate a new password:

`rbw generate {{--no-symbols}} {{--only-numbers}} {{--nonconfusables}} {{password_length}}`

- Lock the vault:

`rbw lock`
