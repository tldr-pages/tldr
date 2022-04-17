# dconf

> Manage dconf databases.
> See also `gsettings`.
> More information: <https://manned.org/dconf.1>.

- Print a specific key value:

`dconf read {{/path/to/key}}`

- Print a specific path sub-directories and sub-keys:

`dconf list {{/path/to/directory/}}`

- Write a specific key value:

`dconf write {{/path/to/key}} "{{value}}"`

- Watch a specific key/directory for changes:

`dconf watch {{/path/to/key|/path/to/directory/}}`

- Dump a specific directory in INI file format:

`dconf dump {{/path/to/directory/}}`
