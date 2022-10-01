# ddev

> Container based local development tool for PHP environments.
> More information: <https://ddev.readthedocs.io>.

- Start up a project:

`ddev start`

- Configure a project's type and docroot:

`ddev config`

- Follow the log trail:

`ddev logs -f`

- Run composer within the container:

`ddev composer`

- Install Node.js version 12:

`ddev nvm install {{version}}`

- Export a database:

`ddev export-db --file=/tmp/db.sql.gz`

- Update the container's apt package lists:

`ddev exec sudo apt-get update`
