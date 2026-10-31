# flatpak install

> Install flatpak applications and runtimes.
> See also: `flatpak`, `flatpak-update`, `flatpak-run`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-install>.

- Install an application from a remote source:

`flatpak install {{remote_name}} {{com.example.app}}`

- Install an application for the current user only:

`flatpak install --user {{remote_name}} {{com.example.app}}`

- Install a specific branch of an application:

`flatpak install {{remote_name}} {{com.example.app}}//{{branch}}`

- Install an application from a `.flatpakref` file or URL:

`flatpak install --from {{path/to/file.flatpakref|https://example.com/file.flatpakref}}`

- Install an application from a `.flatpak` bundle file:

`flatpak install --bundle {{path/to/file.flatpak}}`

- Reinstall an application that is already installed:

`flatpak install --reinstall {{remote_name}} {{com.example.app}}`

- Update an application instead of warning if it is already installed:

`flatpak install --or-update {{remote_name}} {{com.example.app}}`

- Install an application without prompting for confirmation:

`flatpak install --assumeyes {{remote_name}} {{com.example.app}}`
