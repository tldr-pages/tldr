# semanage-user

> Manage SELinux user mappings.
> See also: `semanage`, `semanage-login`.
> More information: <https://manned.org/semanage-user>.

- List all SELinux users:

`sudo semanage user {{[-l|--list]}}`

- Add a new SELinux user:

`sudo semanage user {{[-a|--add]}} {{[-R|--roles]}} "{{staff_r sysadm_r}}" {{myuser_u}}`

- Delete a SELinux user:

`sudo semanage user {{[-d|--delete]}} {{myuser_u}}`

- Modify an existing SELinux user's roles:

`sudo semanage user {{[-m|--modify]}} {{[-R|--roles]}} "{{staff_r}}" {{user_u}}`

- Add a SELinux user with a specific MLS/MCS range:

`sudo semanage user {{[-a|--add]}} {{[-R|--roles]}} {{user_r}} {{[-r|--range]}} {{s0-s0:c0.c1023}} {{guest_u}}`

- List only customized SELinux users:

`sudo semanage user {{[-l|--list]}} {{[-C|--locallist]}}`
