# rpm

> RPM Package Manager.
> More information: <https://rpm.org/>.

- Show version of httpd package:

`rpm --query {{httpd}}`

- List versions of all matching packages:

`rpm --query --all '{{mariadb*}}'`

- Forcibly install a package regardless of currently installed versions:

`rpm --upgrade {{package_name.rpm}} --force`

- Identify owner of a file and show version of the package:

`rpm --query --file {{/etc/postfix/main.cf}}`

- List package-owned files:

`rpm --query --list {{kernel}}`

- Show scriptlets from an RPM file:

`rpm --query --package --scripts {{package_name.rpm}}`

- Show changed, missing and/or incorrectly installed files of matching packages:

`rpm --verify --all '{{php-*}}'`

- Display the changelog of a specific package:

`rpm --query --changelog {{package_name}}`
