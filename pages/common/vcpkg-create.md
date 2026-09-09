# vcpkg create

> Create a new port from a downloadable source archive.
> More information: <https://learn.microsoft.com/vcpkg/commands/create>.

- Create a new port with a specific name from a source archive URL:

`vcpkg create {{port_name}} {{url}}`

- Create a new port using a pre-downloaded source archive:

`vcpkg create {{port_name}} {{url}} {{downloaded_filename}}.zip`
