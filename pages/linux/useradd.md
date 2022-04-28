# useradd

> Create a new user.
> See also: `users`, `userdel`, `usermod`.
> More information: <https://manned.org/useradd>.

- Create a new user:

`sudo useradd {{username}}`

- Create a new user with the specified user id:

`sudo useradd --uid {{id}} {{username}}`

- Create a new user with the specified shell:

`sudo useradd --shell {{path/to/shell}} {{username}}`

- Create a new user belonging to additional groups (mind the lack of whitespace):

`sudo useradd --groups {{group1,group2,...}} {{username}}`

- Create a new user with the default home directory:

`sudo useradd --create-home {{username}}`

- Create a new user with the home directory filled by template directory files:

`sudo useradd --skel {{path/to/template_directory}} --create-home {{username}}`

- Create a new system user without the home directory:

`sudo useradd --system {{username}}`
