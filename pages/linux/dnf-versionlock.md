# dnf versionlock

> Protect packages from updates to newer versions.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/versionlock.html>.

- List the current versionlock entries:

`dnf versionlock`

- Add a versionlock for all available packages matching the spec:

`dnf versionlock add {{package}}`

- Add an exclude (within versionlock) for the available packages matching the spec:

`dnf versionlock exclude {{package}}`

- Remove any matching versionlock entries:

`dnf versionlock delete {{package}}`

- Remove all versionlock entries:

`dnf versionlock clear`
