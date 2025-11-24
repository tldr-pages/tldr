# ya

> Manage Yazi plugins and flavors, publish or subscribe to DDS messages.
> More information: <https://yazi-rs.github.io/docs/cli>.

- Add packages:

`ya pkg add {{PACKAGE}}`

- Delete packages:

`ya pkg delete {{PACKAGE}}`

- Upgrade all packages:

`ya pkg upgrade`

- Emit a command to be executed by the current instance:

`ya emit {{NAME}} {{ARGS}}`

- Subscribe to messages from all remote instances:

`ya sub {{KINDS}}`

- Publish a message to the current instance with string body:

`ya pub --str {{STR}}`
