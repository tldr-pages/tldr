# rpmspec

> Query a RPM spec file.
> More information: <https://manned.org/rpmspec>.

- List binary packages which would be generated from a rpm spec file:

`rpmspec --query {{rpm.spec}}`

- Get summary information for single binary packages generated from rpm spec file:

`rpmspec --query --queryformat "{{%{name}: %{summary}\n}}" {{rpm.spec}}`

- Get the source package which would be generated from the rpm spec file:

`rpmspec --query --srpm {{rpm.spec}}`

- Parse the rpm spec file to `stdout`:

`rpmspec --parse {{rpm.spec}}`
