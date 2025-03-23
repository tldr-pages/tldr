# usermod

> Modify a user account.
> See also: `users`, `useradd`, `userdel`.
> More information: <https://manned.org/usermod>.

- Change a username:

`sudo usermod {{[-l|--login]}} {{new_username}} {{username}}`

- Change a user ID:

`sudo usermod {{[-u|--uid]}} {{id}} {{username}}`

- Change a user shell:

`sudo usermod {{[-s|--shell]}} {{path/to/shell}} {{username}}`

- Add a user to supplementary groups (mind the lack of whitespace):

`sudo usermod {{[-aG|--append --groups]}} {{group1,group2,...}} {{username}}`

- Change a user home directory:

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{path/to/new_home}} {{username}}`

- Lock an account:

`sudo usermod {{[-L|--lock]}} {{username}}`

- Unlock an account:

`sudo usermod {{[-U|--unlock]}} {{username}}`
