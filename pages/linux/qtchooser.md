# qtchooser

> A wrapper used to select between Qt development binary versions.
> More information: <https://manned.org/qtchooser>.

- Lists available Qt versions from the configuration files:

`qtchooser --list-versions`

- Prints environment information:

`qtchooser --print-env`

- Runs the specified tool using the specified Qt version:

`qtchooser --run-tool={{tool}} -qt={{version_name}}`

- Add a Qt version entry to be able to choose from:

`qtchooser --install {{version_name}} {{path/to/qmake}}`

- Output all available options:

`qtchooser --help`
