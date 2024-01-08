# urpmi

> Mageia's command for installing packages.
> See also: `urpm.update`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpmi>.

- Install a package from the repository or from a local RPM file:

`urpmi {{package|path/to/file.rpm}}`

- Update all installed packages (run `urpmi.update -a` to get the available updates):

`urpmi --auto-select`

- Update a package of one or more machines on the network according to `/etc/urpmi/parallel.cfg`:

`urpmi --parallel local {{package}}`
