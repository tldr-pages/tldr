# flatpak

> Build, install and run flatpak applications and runtimes.

- Run an installed application:

`flatpak run {{name}}`

- Install an application from a remote source:

`flatpak install {{remote}} {{name}}`

- List all installed applications and runtimes:

`flatpak list`

- Update all installed applications and runtimes:

`flatpak update`

- Add a remote source:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- List all configured remote sources:

`flatpak remote-list`
