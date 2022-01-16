# useradd

> Create a new user.
> More information: <https://manned.org/useradd>.

- Create a new user:

`useradd {{user}}`

- Create a new user with the specified user id:

`useradd --uid {{id}} {{user}}`

- Create a new user with the specified shell:

`useradd --shell {{path/to/shell}} {{user}}`

- Create a new user belonging to additional groups (mind the lack of whitespace):

`useradd --groups {{group_a,group_b}} {{user}}`

- Create a new user with the default home directory:

`useradd --create-home {{user}}`

- Create a new user with the home directory filled by template directory files:

`useradd --skel {{path/to/template_directory}} --create-home {{user}}`

- Create a new system user without the home directory:

`useradd --system {{user}}`
