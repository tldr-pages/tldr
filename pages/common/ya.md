# ya

> Manage Yazi packages and plugins.
> More information: <https://github.com/sxyazi/yazi>.

- Add a package:

`ya pack {{[-a|--all]}} {{package}}`

- Upgrade all packages:

`ya pack {{[-u|--upgrade]}}`

- Subscribe to messages from all remote instances:

`ya sub {{kinds}}`

- Publish a message to the current instance with string body:

`ya pub --str {{string_message}}`

- Publish a message to the current instance with JSON body:

`ya pub --json {{json_message}}`

- Publish a message to the specified instance with string body:

`ya pub-to --str {{message}} {{receiver}} {{kind}}`
