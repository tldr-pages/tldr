# useradd

> Create a new user.
> More information: <https://manned.org/useradd>.

- Create a new user:

`useradd {{user_name}}`

- Create a new user with the specified user id:

`useradd --uid {{user_id}} {{user_name}}`

- Create a new user with the specified shell:

`useradd --shell {{path/to/shell}} {{user_name}}`

- Create a new user belonging to additional groups (mind the lack of whitespace):

`useradd --groups {{group_a,group_b}} {{user_name}}`

- Create a new user with the default home directory:

`useradd --create-home {{user_name}}`

- Create a new user with the home directory filled by template directory files:

`useradd --skel {{path/to/template_directory}} --create-home {{user_name}}`

- Create a new system user without the home directory:

`useradd --system {{user_name}}`
