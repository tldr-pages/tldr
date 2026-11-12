# flatpak remote-add

> Add a remote repository to the Flatpak configuration.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-add>.

- Add a remote repository:

`flatpak remote-add {{remote_name}} {{remote_url}}`

- Add a remote repository only if it does not exist yet:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- Add a remote repository for the current user only:

`flatpak remote-add {{[-u|--user]}} {{remote_name}} {{remote_url}}`

- Add a remote repository from a `.flatpakrepo` file or URL:

`flatpak remote-add {{remote_name}} {{path/to/file.flatpakrepo|https://example.com/file.flatpakrepo}}`
