# dnf install

> Install packages on Red Hat-based distributions.
> More information: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- Install packages by name:

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- Install a package from a local file:

`sudo dnf {{[in|install]}} {{path/to/file}}`

- Install a package from the internet:

`sudo dnf {{[in|install]}} {{https://example.com/package.rpm}}`

- Add the Extra Packages for Enterprise Linux (EPEL) repositories:

`sudo dnf {{[in|install]}} https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{10}}.noarch.rpm`

- Add Remi's RPM repository:

`sudo dnf {{[in|install]}} https://rpms.remirepo.net/enterprise/remi-release-{{8}}.rpm`
