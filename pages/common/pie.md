# pie

> The PHP Installer for Extensions.
> More information: <https://github.com/php/pie/blob/main/docs/usage.md>.

- Install or update an extension:

`pie install {{vendor}}/{{extension}}`

- List installed extensions and their versions:

`pie show`

- Display information about a specific package:

`pie info {{vendor}}/{{extension}}`

- List the configured repositories:

`pie repository:list`

- Add a repository:

`pie repository:add {{type}} {{url}}`

- Remove a repository:

`pie repository:remove {{url}}`
