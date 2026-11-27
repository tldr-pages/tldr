# apt clean

> Clear the local repository of retrieved package files.
> More information: <https://manned.org/apt.8>.

- Remove all downloaded package files from the local cache:

`sudo apt clean`

- Simulate clearing the package cache without deleting files:

`apt clean {{[-s|--simulate]}}`

- Clear package files quietly, producing output suitable for logging:

`sudo apt clean {{[-q|--quiet]}}`

- Clear package files using a custom configuration file:

`sudo apt clean {{[-c|--config-file]}} {{path/to/apt.conf}}`

- Clear package files from a specific cache directory:

`sudo apt clean -o {{Dir::Cache::Archives}}={{path/to/directory}}`
