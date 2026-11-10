# flatpak uninstall

> Uninstall flatpak applications and runtimes.
> See also: `flatpak install`, `flatpak update`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-uninstall>.

- Uninstall an application or runtime:

`flatpak uninstall {{com.example.app}}`

- Uninstall an application from the per-user installation:

`flatpak uninstall {{[-u|--user]}} {{com.example.app}}`

- Uninstall an application and delete its data in `~/.var/app`:

`flatpak uninstall --delete-data {{com.example.app}}`

- Uninstall all unused applications and runtimes:

`flatpak uninstall --unused`

- Delete the data of all applications that are no longer installed:

`flatpak uninstall --delete-data`

- Uninstall an application without prompting for confirmation:

`flatpak uninstall {{[-y|--assumeyes]}} {{com.example.app}}`

- Uninstall all applications and runtimes:

`flatpak uninstall --all`
