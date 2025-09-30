# eim

> ESP-IDF Installation Manager (EIM): Unified tool to install and manage ESP-IDF.
> More information: <https://docs.espressif.com/projects/idf-im-ui/en/latest/>.

- Install default (latest) ESP-IDF version on default location:

`eim install`

- Install a specific ESP-IDF version non-interactively (default headless mode):

`eim install -i {{v5.3.2}}`

- Run the interactive, guided installation wizard:

`eim wizard`

- Install a specific version to a custom path, forcing interactive mode (to prompt for choices):

`eim install -i {{v5.3.2}} -p {{/opt/esp-idf}} -n false`

- List all currently installed ESP-IDF versions:

`eim list`

- Remove a specific installed ESP-IDF version:

`eim remove {{v5.3.2}}`

- Install in headless mode using all options defined in a TOML configuration file:

`eim install --config {{path/to/config.toml}}`

- Install offline using a pre-downloaded archive file:

`eim install --use-local-archive {{path/to/archive.zst}}`
