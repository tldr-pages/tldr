# semanage-login

> Manage SELinux login mappings between Linux users and SELinux users.
> See also: `semanage`, `semanage-user`.
> More information: <https://manned.org/semanage-login>.

- List all login mappings:

`sudo semanage login {{[-l|--list]}}`

- Add a login mapping (map Linux user to SELinux user):

`sudo semanage login {{[-a|--add]}} {{[-s|--seuser]}} {{user_u}} {{username}}`

- Delete a login mapping:

`sudo semanage login {{[-d|--delete]}} {{username}}`

- Modify an existing login mapping:

`sudo semanage login {{[-m|--modify]}} {{[-s|--seuser]}} {{staff_u}} {{username}}`

- Add a login mapping with a specific MLS/MCS range:

`sudo semanage login {{[-a|--add]}} {{[-s|--seuser]}} {{user_u}} {{[-r|--range]}} {{s0-s0:c0.c1023}} {{username}}`

- List only customized login mappings:

`sudo semanage login {{[-l|--list]}} {{[-C|--locallist]}}`
