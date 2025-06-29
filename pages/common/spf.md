# spf

> The superfile – Modern terminal file manager.
> More information: <https://github.com/yorukot/superfile>.

- Launch `spf` with a specific path:

`spf {{path/to/directory}}`

- Launch `spf` with multiple paths:

`spf {{path/to/directory1 path/to/directory2 ...}}`

- Fix hotkey settings by appending missing keys:

`spf {{[--fh|--fix-hotkeys]}}`

- Fix the configuration file by appending missing entries:

`spf {{[--fch|--fix-config-file]}}`

- Use specific configuration and hotkey files:

`spf {{[-c|--config-file]}} {{path/to/config.toml}} {{[--hf|--hotkey-file]}} {{path/to/hotkey.toml}}`

- Write the path of the first selected file to this file and exit:

`spf {{[--cf|--chooser-file]}} {{tmp/chooser-result}}`

- Show internal configuration and data directory paths:

`spf {{[pl|path-list]}}`
