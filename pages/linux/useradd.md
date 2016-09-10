# useradd

> Create a new user.

- Create new user:

`useradd {{name}}`

- Create new user with a default home directory:

`useradd -m {{name}}`

- Create new user with specified shell:

`useradd -s {{/path/to/shell}} {{name}}`

- Create new user with supplementary groups (mind the lack of whitespace):

`useradd -G {{group1,group2}} {{name}}`

- Create new system user without a home directory:

`useradd --no-create-home --system {{name}}`
