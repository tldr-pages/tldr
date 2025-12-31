# rpm

> RPM Package Manager.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://rpm-software-management.github.io/rpm/man/rpm.8>.

- Show version of httpd package:

`rpm {{[-q|--query]}} httpd`

- List versions of all matching packages:

`rpm {{[-qa|--query --all]}} '{{mariadb*}}'`

- Forcibly install a package regardless of currently installed versions:

`rpm {{[-U|--upgrade]}} {{path/to/package.rpm}} --force`

- Identify owner of a file and show version of the package:

`rpm {{[-qf|--query --file]}} {{/etc/postfix/main.cf}}`

- List package-owned files:

`rpm {{[-ql|--query --list]}} {{kernel}}`

- Show scriptlets from an RPM file:

`rpm {{[-qp|--query --package]}} --scripts {{package.rpm}}`

- Show changed, missing and/or incorrectly installed files of matching packages:

`rpm {{[-Va|--verify --all]}} '{{php-*}}'`

- Display the changelog of a specific package:

`rpm {{[-q|--query]}} --changelog {{package}}`
