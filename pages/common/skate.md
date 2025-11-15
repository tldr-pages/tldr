# skate

> Simple and powerful key-value store.
> More information: <https://github.com/charmbracelet/skate>.

- Store a key and a value on the default database:

`skate set "{{key}}" "{{value}}"`

- Show your keys saved on the default database:

`skate list`

- Delete key and value from the default database:

`skate delete "{{key}}"`

- Create a new key and value in a new database:

`skate set "{{key}}"@"{{database_name}}" "{{value}}"`

- Show your keys saved in a non default database:

`skate list @"{{database_name}}"`

- Delete key and value from a specific database:

`skate delete "{{key}}"@"{{database_name}}"`

- Show the databases available:

`skate list-dbs`

- Delete local db and pull down fresh copy from Charm Cloud:

`skate reset @"{{database_name}}"`
