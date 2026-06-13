# mas

> Command-line interface for the Mac App Store.
> More information: <https://github.com/mas-cli/mas>.

- Sign into the Mac App Store for the first time:

`mas signin "{{user@example.com}}"`

- Show all installed applications and their product identifiers:

`mas list`

- Search for an application, displaying the price alongside the results:

`mas search "{{application}}" --price`

- Install or update an application using exact numeric id:

`mas install {{numeric_product_id}}`

- Install the first application that would be returned by the respective search:

`mas lucky "{{search_term}}"`

- List all outdated apps with pending updates:

`mas outdated`

- Install all pending updates:

`mas upgrade`

- Upgrade a specific application:

`mas upgrade "{{numeric_product_id}}"`
