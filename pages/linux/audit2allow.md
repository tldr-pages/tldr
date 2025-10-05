# audit2allow

> Generate SELinux policy allow rules from audit logs.
> Part of the `policycoreutils-python-utils` package.
> See also: `audit2why`, `ausearch`, `semodule`.
> More information: <https://manned.org/audit2allow>.

- Generate allow rules from recent audit denials and display them:

`sudo audit2allow -a`

- Generate allow rules from a specific audit log file:

`sudo audit2allow -i {{path/to/audit.log}}`

- Generate a policy module from recent audit denials:

`sudo audit2allow -a -M {{my_module}}`

- Install the generated policy module:

`sudo semodule -i {{my_module.pp}}`

- Generate allow rules for a specific service:

`sudo ausearch -m avc -c {{httpd}} | audit2allow -M {{httpd_policy}}`
