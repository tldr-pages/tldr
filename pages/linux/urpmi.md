# urpmi

> Install packages in Mageia.
> See also: `urpm.update`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpmi>.

- Install a package from the repository or from a local RPM file:

`sudo urpmi {{package|path/to/file.rpm}}`

- Download a package without installing it:

`urpmi --no-install {{package}}`

- Update all installed packages (run `urpmi.update -a` to get the available updates):

`sudo urpmi --auto-select`

- Update a package of one or more machines on the network according to `/etc/urpmi/parallel.cfg`:

`sudo urpmi --parallel local {{package}}`

- Mark all orphaned packages as manually installed:

`sudo urpmi $(urpmq --auto-orphans -f)`
