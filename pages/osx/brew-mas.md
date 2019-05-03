# brew mas

> Mas is a simple command line interface for the Mac App Store.
> Homepage: <https://github.com/mas-cli/mas>.

- Search the Mac App Store by app name and return matching identifiers:

`mas search {{app_name}}`

- Install or update a previously purchased application:

`mas install {{app_name}} {{app_identifier}}`

- Show all installed applications and their product identifiers:

`mas list`

- List installed apps with pending updates:

`mas outdated`

- Install all pending updates:

`mas upgrade`

- Install updates for a specific app:

`mas upgrade {{app_identifier}}`
