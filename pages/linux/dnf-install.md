# dnf install

> Install packages on Red Had based distributions.
> More information: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- Install a package by name:

`sudo dnf install {{package1 package2 ...}}`

- Install a package from a local file:

`sudo dnf install {{path/to/file}}`

- Install a package from the internet:

`sudo dnf install {{https://example.com/package.rmp}}`

- Add the Extra Packages for Enterprise Linux (EPEL) repositories:

`dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm`

- Add Remi's RPM repository:

`dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm`
