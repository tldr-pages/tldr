# flatpak

> Build, install and run flatpak applications and runtimes.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Run an installed application:

`flatpak run {{com.example.app}}`

- Install an application from a remote source:

`flatpak install {{remote_name}} {{com.example.app}}`

- List installed applications, ignoring runtimes:

`flatpak list --app`

- Update all installed applications and runtimes:

`flatpak update`

- Add a remote source:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- Remove an installed application:

`flatpak remove {{com.example.app}}`

- Remove all unused applications:

`flatpak remove --unused`

- Show information about an installed application:

`flatpak info {{com.example.app}}`
