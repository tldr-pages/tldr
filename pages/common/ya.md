# ya

> Yazi command-line interface.
> Manage yazi packages and plugins.
> More information: <https://github.com/sxyazi/yazi>.

- Add a package:

`ya pack -a {{PACKAGE}}`

- Upgrade all packages:

`ya pack -u`

- Subscribe to messages from all remote instances:

`ya sub {{KINDS}}`

- Publish a message to the current instance with string body:

`ya pub --str {{STR}}`

- Publish a message to the specified instance with string body:

`ya pub-to --str {{STR}} {{RECEIVER}} {{KIND}}`
