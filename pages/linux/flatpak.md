# flatpak

> Build, install and run flatpak applications and runtimes.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Run an installed application:

`flatpak run {{name}}`

- Install an application from a remote source:

`flatpak install {{remote}} {{name}}`

- List installed applications, ignoring runtimes:

`flatpak list --app`

- Update all installed applications and runtimes:

`flatpak update`

- Add a remote source:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- Remove an installed application:

`flatpak remove {{name}}`

- Remove all unused applications:

`flatpak remove --unused`

- Show information about an installed application:

`flatpak info {{name}}`
