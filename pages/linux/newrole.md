# newrole

> Run a new shell with a different SELinux role.
> Allows users to switch to a different SELinux security context.
> See also: `runcon`, `semanage-user`.
> More information: <https://manned.org/newrole>.

- Start a new shell with a specific SELinux role:

`newrole {{[-r|--role]}} {{role_name}}`

- Start a new shell with a specific SELinux type:

`newrole -t {{type_name}}`

- Start a new shell with a specific SELinux level:

`newrole -l {{s0-s0:c0.c1023}}`

- Display the current SELinux context:

`id -Z`

- Start a new shell with both role and type:

`newrole -r {{role_name}} -t {{type_name}}`
