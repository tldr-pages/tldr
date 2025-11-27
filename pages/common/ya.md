# ya

> Manage Yazi plugins and flavors, publish or subscribe to DDS messages.
> More information: <https://yazi-rs.github.io/docs/cli>.

- Add a package:

`ya pkg add {{package}}`

- Delete a package:

`ya pkg delete {{package}}`

- Upgrade all packages:

`ya pkg upgrade`

- List all packages:

`ya pkg list`

- Emit a command to be executed by the current instance:

`ya emit {{name}} {{args}}`

- Publish a message to the current instance with string body:

`ya pub --str {{str}}`
