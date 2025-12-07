# id

> Display current user and group identity.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/id-invocation.html>.

- Display current user's ID (UID), group ID (GID) and groups to which they belong:

`id`

- Display the current user identity:

`id {{[-un|--user --name]}}`

- Display the current user identity as a number:

`id {{[-u|--user]}}`

- Display the current primary group identity:

`id {{[-gn|--group --name]}}`

- Display the current primary group identity as a number:

`id {{[-g|--group]}}`

- Display an arbitrary user's ID (UID), group ID (GID) and groups to which they belong:

`id {{username}}`

- Skip name lookup and specify the UID number explicitly:

`id +{{uid_number}}`
