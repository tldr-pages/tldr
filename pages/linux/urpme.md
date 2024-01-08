# urpme

> Mageia's command for uninstalling packages.
> See also: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpme>.

- Uninstall a package:

`urpme {{package}}`

- Uninstall orphan packages (warning: it's very easy to unintentionally remove important packages):

`urpme --auto-orphans`

- Uninstall a package and its dependecies:

`urpme --auto-orphans {{package}}`
