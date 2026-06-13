# semanage-login

> Manage SELinux login mappings between Linux users and SELinux users.
> See also: `semanage`, `semanage-user`.
> More information: <https://manned.org/semanage-login>.

- List all login mappings:

`sudo semanage login {{[-l|--list]}}`

- Add a login mapping (map Linux user to SELinux user):

`sudo semanage login {{[-a|--add]}} {{[-s|--seuser]}} {{selinux_user}} {{linux_username}}`

- Delete a login mapping:

`sudo semanage login {{[-d|--delete]}} {{linux_username}}`

- Modify an existing login mapping:

`sudo semanage login {{[-m|--modify]}} {{[-s|--seuser]}} {{selinux_user}} {{linux_username}}`

- Add a login mapping with a specific MLS/MCS range:

`sudo semanage login {{[-a|--add]}} {{[-s|--seuser]}} {{user_u}} {{[-r|--range]}} {{s0-s0:c0.c1023}} {{linux_username}}`

- List only customized login mappings:

`sudo semanage login {{[-l|--list]}} {{[-C|--locallist]}}`
