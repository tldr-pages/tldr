# pyats

> Cisco's vendor-agnostic test automation framework for network and systems validation.
> More information: <https://developer.cisco.com/docs/pyats/api/>.

- Run a test job from a Python file:

`pyats run job {{path/to/job_file.py}}`

- Parse the output of a show command from a device:

`pyats parse "show version" --testbed {{path/to/testbed.yaml}}`

- List all available parsers or testbeds:

`pyats list`

- Check the current version:

`pyats version check`

- Display help for a subcommand:

`pyats {{subcommand}} --help`
