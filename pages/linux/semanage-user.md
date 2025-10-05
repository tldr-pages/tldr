# semanage-user

> Manage SELinux user mappings.
> See also: `semanage`, `semanage-login`.
> More information: <https://manned.org/semanage-user>.

- List all SELinux users:

`sudo semanage user {{[-l|--list]}}`

- Add a new SELinux user:

`sudo semanage user --add --roles {{role_name}} {{selinux_user}}`

- Delete a SELinux user:

`sudo semanage user --delete {{selinux_user}}`

- Modify an existing SELinux user's roles:

`sudo semanage user --modify --roles {{role_name}} {{selinux_user}}`

- Add a SELinux user with a specific MLS/MCS range:

`sudo semanage user --add --roles {{role_name}} --range {{s0-s0:c0.c1023}} {{selinux_user}}`

- List only customized SELinux users:

`sudo semanage user --list --locallist`
