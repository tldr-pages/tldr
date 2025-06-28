# spf

> The superfile – Modern terminal file manager.
> More information: <https://github.com/yorukot/superfile>.

- Launch `spf` with a specific path:

`spf {{/path/to/start}}`

- Launch `spf` with multiple paths:

`spf {{/path/to/start1}} {{/path/to/start2}}`

- Fix hotkey settings by appending missing keys:

`spf {{[-fh|--fix-hotkeys]}}`

- Fix the configuration file by appending missing entries:

`spf --fix-config-file`

- Use specific configuration and hotkey files:

`spf {{[-c|--config-file]}} {{path/to/config.toml}} {{[--hf|--hotkey-file]}} {{path/to/hotkey.toml}}`

- Set a chooser file: write the opened path to this file and exit:

`spf {{[--cf|--chooser-file]}} {{/tmp/chooser-result}}`

- Show internal configuration and data directory paths:

`spf {{[pl|path-list]}}`
