# newrole

> Run a new shell with a different SELinux role.
> Allows users to switch to a different SELinux security context.
> See also: `runcon`, `semanage-user`.
> More information: <https://manned.org/newrole>.

- Start a new shell with a specific SELinux role:

`newrole {{[-r|--role]}} {{role_name}}`

- Start a new shell with a specific SELinux type:

`newrole {{[-t|--type]}} {{type_name}}`

- Start a new shell with a specific SELinux level (format: `s0-s0:c0.c1023` where levels range from `s0` to `s15`, `-` indicates level range, categories start with `c`, `:` separates level from categories, `.` indicates category range):

`newrole {{[-l|--level]}} {{s0-s0:c0.c1023}}`

- Display the current SELinux context:

`id {{[-Z|--context]}}`

- Start a new shell with both role and type:

`newrole {{[-r|--role]}} {{role_name}} {{[-t|--type]}} {{type_name}}`
