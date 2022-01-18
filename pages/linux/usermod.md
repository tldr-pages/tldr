# usermod

> Modifies a user account.
> More information: <https://manned.org/usermod>.

- Change a username:

`usermod --login {{new_username}} {{username}}`

- Change a user id:

`usermod --uid {{id}} {{username}}`

- Change a user shell:

`usermod --shell {{path/to/shell}} {{username}}`

- Add a user to supplementary groups (mind the lack of whitespace):

`usermod --append --groups {{group1,group2,...}} {{username}}`

- Change a user home directory:

`usermod --move-home --home {{path/to/new_home}} {{username}}`
