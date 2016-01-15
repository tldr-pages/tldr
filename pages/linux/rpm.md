# rpm

> RPM Package Manager

- Show version of httpd package:

`rpm -q {{httpd}}`

- List versions of all matching packages:

`rpm -qa '{{mariadb*}}'`

- Identify owner of a file and show version of the package:

`rpm -qf {{/etc/postfix/main.cf}}`

- List package-owned files:

`rpm -ql {{kernel}}`

- List configuration, then only documentation files of httpd:

`rpm -qlc {{httpd}}`
`rpm -qld {{httpd}}`

- show contents of an RPM file:

`rpm -qlp {{some.rpm}}`

- Show scriptlets from an RPM file:

`rpm -qp --scripts {{some.rpm}}`

- Show capabilities provided by an RPM file

`rpm -qp --provides {{some.rpm}}`

- Show capabilities needed by an RPM file

`rpm -qp --requires {{some.rpm}}`

- Show changed, missing and/or incorrectly installed files of matching packages:

`rpm -Va '{{php-*}}'`A

- Show metadata about a package's files "intended" properties:

`rpm --dump -q {{php-pear}}`
