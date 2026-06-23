# archinstall

> Guided Arch Linux installer.
> More information: <https://archinstall.archlinux.page/installing/guided.html>.

- Start the interactive installer:

`archinstall`

- Start the interactive installer and generate a configuration file instead of installing:

`archinstall --dry-run`

- Enable advanced options:

`archinstall --advanced`

- Install using the specified configuration files:

`archinstall --config {{path/to/config.json}} --creds {{path/to/credentials.json}}`

- Install using configuration files from a remote server:

`archinstall --config-url {{https://example.com/config.json}} --creds-url {{https://example.com/credentials.json}}`

- Install using the specified script:

`archinstall --script {{minimal|only_hd}}`
