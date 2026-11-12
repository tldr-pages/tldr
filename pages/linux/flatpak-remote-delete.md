# flatpak remote-delete

> Remove a remote repository from the Flatpak configuration.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-delete>.

- Remove a remote repository:

`flatpak remote-delete {{remote_name}}`

- Remove a remote repository from the per-user configuration:

`flatpak remote-delete {{[-u|--user]}} {{remote_name}}`

- Remove a remote repository from the default system-wide configuration:

`flatpak remote-delete --system {{remote_name}}`

- Force the removal of a remote repository currently in use:

`flatpak remote-delete --force {{remote_name}}`
