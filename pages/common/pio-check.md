# pio check

> Perform a static analysis check on a PlatformIO project.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- Perform a basic analysis check on the current project:

`pio check`

- Perform a basic analysis check on a specific project:

`pio check --project-dir {{project_dir}}`

- Perform an analysis check for a specific environment:

`pio check --environment {{environment}}`

- Perform an analysis check and only report a specified defect severity type:

`pio check --severity {{low|medium|high}}`

- Perform an analysis check and show detailed information when processing environments:

`pio check --verbose`
