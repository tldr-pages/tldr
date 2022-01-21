# mas

> Command-line interface for the Mac App Store.
> More information: <https://github.com/mas-cli/mas>.

- Sign into the Mac App Store for the first time:

`mas signin "{{user@example.com}}"`

- Show all installed applications and their product identifiers:

`mas list`

- Search for an application, displaying the price alongside the results:

`mas search "{{application}}" --price`

- Install or update an application:

`mas install {{product_identifier}}`

- Install all pending updates:

`mas upgrade`
