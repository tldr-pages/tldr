# plesk

> Plesk hosting control panel CLI interface.
> More information: <https://docs.plesk.com>.

- Generate an auto login link for the admin user and print it:

`plesk login`

- Show product version information:

`plesk version`

- List all hosted domains:

`plesk bin domain --list`

- Start watching for changes in the `panel.log` file:

`plesk log {{panel.log}}`

- Start the interactive MySQL console:

`plesk db`

- Open the Plesk main configuration file in the default editor:

`plesk conf {{panel.ini}}`
