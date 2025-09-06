# openocd

> Debug and program embedded systems with OpenOCD.
> More information: <https://manned.org/openocd>.

- Attach OpenOCD session to a board with a configuration file:

`openocd {{[-f|--file]}} {{config_file.cfg}}`

- Attach OpenOCD session to a board with multiple configuration files:

`openocd {{[-f|--file]}} {{config_file1.cfg}} {{[-f|--file]}} {{config_file2.cfg}}`

- Attach OpenOCD session to a board with configuration files and a list of commands to be executed on server startup:

`openocd {{[-f|--file]}} {{config_file.cfg}} {{[-c|--command]}} "{{command}}"`

- Use configuration files in the specified path:

`openocd {{[-s|--search]}} {{path/to/search}} {{[-f|--file]}} {{config_file.cfg}}`

- After OpenOCD startup, connect GDB to OpenOCD default port 3333:

`target extended-remote localhost`

- List site-wide script library:

`ls /usr/local/share/openocd/scripts`
