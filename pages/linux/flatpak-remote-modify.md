# flatpak remote-modify

> Modify the options of an existing remote repository.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-modify>.

- Change the URL of a remote repository:

`flatpak remote-modify --url {{remote_url}} {{remote_name}}`

- Disable a remote repository:

`flatpak remote-modify --disable {{remote_name}}`

- Enable a remote repository:

`flatpak remote-modify --enable {{remote_name}}`

- Modify a remote repository in the per-user configuration:

`flatpak remote-modify {{[-u|--user]}} --disable {{remote_name}}`
