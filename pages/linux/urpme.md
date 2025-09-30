# urpme

> Uninstall packages in Mageia.
> See also: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> More information: <https://man.linuxreviews.org/man8/urpme.8.html>.

- Uninstall a package:

`sudo urpme {{package}}`

- Uninstall orphan packages (Note: Use it with caution as it might unintentionally remove important packages):

`sudo urpme --auto-orphans`

- Uninstall a package and its dependencies:

`sudo urpme --auto-orphans {{package}}`
