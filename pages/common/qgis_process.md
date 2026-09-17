# qgis_process

> Run QGIS processing algorithms from the command line without opening the GUI.
> See also: `qgis`.
> More information: <https://docs.qgis.org/latest/en/docs/user_manual/processing/standalone.html>.

- List all available processing algorithms:

`qgis_process list`

- Display help for a specific algorithm:

`qgis_process help {{algorithm_id}}`

- Run a processing algorithm with parameters:

`qgis_process run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- Run an algorithm and output results as JSON:

`qgis_process --json run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- Run without loading plugins for faster startup:

`qgis_process --skip-loading-plugins run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- Run on a headless server without a display:

`QT_QPA_PLATFORM=offscreen qgis_process run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- List available and active plugins:

`qgis_process plugins`

- Enable or disable an installed plugin:

`qgis_process plugins {{enable|disable}} {{plugin_name}}`
