# usermod

> Modifies a user account.
> See also: `users`, `useradd`, `userdel`.
> More information: <https://manned.org/usermod>.

- Change a username:

`sudo usermod --login {{new_username}} {{username}}`

- Change a user ID:

`sudo usermod --uid {{id}} {{username}}`

- Change a user shell:

`sudo usermod --shell {{path/to/shell}} {{username}}`

- Add a user to supplementary groups (mind the lack of whitespace):

`sudo usermod --append --groups {{group1,group2,...}} {{username}}`

- Change a user home directory:

`sudo usermod --move-home --home {{path/to/new_home}} {{username}}`
