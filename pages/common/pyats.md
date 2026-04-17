# pyats

> A Python-based network test and automation framework.
> Some subcommands such as `run`, `shell`, and `parse` have their own usage documentation.
> More information: <https://developer.cisco.com/docs/pyats/>.

- Run a pyATS testscript or a job file:

`pyats run job {{path/to/script_or_job.py}}`

- Open a Python shell with the pyATS environment loaded:

`pyats shell --testbed-file {{path/to/testbed.yaml}}`

- Parse the output of a router `show` command using Genie parsers:

`pyats parse "{{show_command}}" --testbed-file {{path/to/testbed.yaml}} --device {{device_name}}`

- Learn and profile device features (e.g., OSPF, BGP) using Genie:

`pyats learn {{feature}} --testbed-file {{path/to/testbed.yaml}} --device {{device_name}}`

- Save the parsed output to a specific directory:

`pyats parse "{{show_command}}" --testbed-file {{path/to/testbed.yaml}} --device {{device_name}} --output {{path/to/directory}}`

- Create a template testbed YAML file or Python script:

`pyats create {{testbed|script}}`

- Display help for a subcommand:

`pyats {{run|shell|parse|learn|create}} --help`
