# useradd

> Create a new user.
> See also: `users`, `userdel`, `usermod`.
> More information: <https://manned.org/useradd>.

- Create a new user:

`sudo useradd {{username}}`

- Create a new user with the specified user ID:

`sudo useradd {{[-u|--uid]}} {{id}} {{username}}`

- Create a new user with the specified shell:

`sudo useradd {{[-s|--shell]}} {{path/to/shell}} {{username}}`

- Create a new user belonging to additional groups (mind the lack of whitespace):

`sudo useradd {{[-G|--groups]}} {{group1,group2,...}} {{username}}`

- Create a new user with the default home directory:

`sudo useradd {{[-m|--create-home]}} {{username}}`

- Create a new user with the home directory filled by template directory files:

`sudo useradd {{[-k|--skel]}} {{path/to/template_directory}} {{[-m|--create-home]}} {{username}}`

- Create a new system user without the home directory:

`sudo useradd {{[-r|--system]}} {{username}}`
