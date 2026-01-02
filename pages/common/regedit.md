# regedit

> Wine registry counterpart of the Microsoft Windows `regedit` service.
> More information: <https://manned.org/regedit>.

- Export a specific registry key and contents to a file:

`regedit -E {{path/to/file}} {{path/to/registry_key}}`

- Delete a specified registry key:

`regedit -D {{path/to/registry_key}}`

- Display help:

`regedit -?`
