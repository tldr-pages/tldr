# pio project

> Tool to manage a PlatformIO project.
> More information: <https://docs.platformio.org/en/latest/core/userguide/project/index.html>.

- Initialize a new PlatformIO based project (when omitting `--project-dir`, it will default to the current working directory):

`pio project init --project-dir {{path/to/project_directory}}`

- Initialize a new PlatformIO based project, specifying a board ID and several project options (when omitting `--project-dir`, it will default to the current working directory):

`pio project init --project-dir {{path/to/project_directory}} --board {{board_id}} --project-option="{{option}}={{value}}}" --project-option="{{option}}={{value}}"`

- Print configurations of a specific project (when omitting `--project-dir`, it will default to the current working directory):

`pio project config --project-dir {{path/to/project_directory}}`

- Print data of a specific project, intended for IDE extensions/plugins (when omitting `--project-dir`, it will default to the current working directory):

`pio project data --project-dir {{path/to/project_directory}}`
