# eim

> Install and manage ESP-IDF.
> More information: <https://docs.espressif.com/projects/idf-im-ui/en/latest/cli_commands.html>.

- Install the default (latest) ESP-IDF version in the default location (`C:\esp` on Windows and `~/.espressif` on POSIX systems):

`eim install`

- Install a specific ESP-IDF version:

`eim install {{[-i|--idf-versions]}} {{v5.3.2}}`

- Run the interactive, guided installation wizard:

`eim wizard`

- Install a specific version to a custom path, forcing interactive mode (to prompt for choices):

`eim install {{[-i|--idf-versions]}} {{v5.3.2}} {{[-p|--path]}} {{/opt/esp-idf}} {{[-n|--non-interactive]}} false`

- List all currently installed ESP-IDF versions:

`eim list`

- Remove a specific installed ESP-IDF version:

`eim remove {{v5.3.2}}`

- Install in headless mode using all options defined in a TOML configuration file:

`eim install {{[-c|--config]}} {{path/to/config.toml}}`

- Install offline using a pre-downloaded archive file:

`eim install --use-local-archive {{path/to/archive.zst}}`
