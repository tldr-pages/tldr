# rpm

> RPM Package Manager.

- Show version of httpd package:

`rpm -q {{httpd}}`

- List versions of all matching packages:

`rpm -qa '{{mariadb*}}'`

- Identify owner of a file and show version of the package:

`rpm -qf {{/etc/postfix/main.cf}}`

- List package-owned files:

`rpm -ql {{kernel}}`

- Show scriptlets from an RPM file:

`rpm -qp --scripts {{some.rpm}}`

- Show changed, missing and/or incorrectly installed files of matching packages:

`rpm -Va '{{php-*}}'`
