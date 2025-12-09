# pio check

> Perform a static analysis check on a PlatformIO project.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- Perform a basic analysis check on the current project:

`pio check`

- Perform a basic analysis check on a specific project:

`pio check {{[-d|--project-dir]}} {{project_directory}}`

- Perform an analysis check for a specific environment:

`pio check {{[-e|--environment]}} {{environment}}`

- Perform an analysis check and only report a specified defect severity type:

`pio check --severity {{low|medium|high}}`

- Perform an analysis check and show detailed information when processing environments:

`pio check {{[-v|--verbose]}}`
