# dnf repoquery

> Query packages from the enabled repositories.
> More information: <https://dnf5.readthedocs.io/en/latest/commands/repoquery.8.html>.

- List the capabilities a package requires:

`dnf repoquery --requires {{package}}`

- List packages that require a capability or package:

`dnf repoquery --whatrequires {{package}}`

- List packages that provide a given file:

`dnf repoquery /{{path/to/file}}`

- Show detailed information about a package:

`dnf repoquery --info {{package}}`
