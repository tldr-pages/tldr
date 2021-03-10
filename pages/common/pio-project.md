# pio project

> Tool to manage PlatformIO projects.
> More information: <https://docs.platformio.org/en/latest/core/userguide/project/index.html>.

- Initialize a new PlatformIO based project (defaults to current directory if `--project-dir` is omitted):

`pio project init --project-dir {{path/to/project_directory}}`

- Initialize a new PlatformIO based project, specifying a board ID and several project options:

`pio project init --project-dir {{path/to/project_directory}} --board {{board_id}} --project-option="{{option}}={{value}}}" --project-option="{{option}}={{value}}"`

- Print configurations of a specific project:

`pio project config --project-dir {{path/to/project_directory}}`

- Print data of a specific project, intended for IDE extensions/plugins:

`pio project data --project-dir {{path/to/project_directory}}`
