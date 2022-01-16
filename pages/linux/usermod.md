# usermod

> Modifies a user account.
> More information: <https://manned.org/usermod>.

- Change a user name:

`usermod --login {{new_user}} {{user}}`

- Change a user id:

`usermod --uid {{id}} {{user}}`

- Change a user shell:

`usermod --shell {{path/to/shell}} {{user}}`

- Add a user to supplementary groups (mind the lack of whitespace):

`usermod --append --groups {{group_a,group_b}} {{user}}`

- Change a user home directory:

`usermod --move-home --home {{path/to/new_home}} {{user}}`
