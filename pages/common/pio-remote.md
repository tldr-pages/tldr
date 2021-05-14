# pio remote

> Helper command for PlatformIO Remote Development.
> `pio remote [command]` takes the same arguments as its locally executing counterpart `pio [command]`.
> More information: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

- List all active Remote Agents:

`pio remote agent list`

- Start a new Remote Agent with a specific name and share it with friends:

`pio remote agent start --name {{agent_name}} --share {{example1@example.com}} --share {{example2@example.com}}`

- List devices from specified Agents (omit `--agent` to specify all Agents):

`pio remote --agent {{agent_name1}} --agent {{agent_name2}} device list`

- Connect to the serial port of a remote device:

`pio remote --agent {{agent_name}} device monitor`

- Run all targets on a specified Agent:

`pio remote --agent {{agent_name}} run`

- Update installed core packages, development platforms and global libraries on a specific Agent:

`pio remote --agent {{agent_name}} update`

- Run all tests in all environments on a specific Agent:

`pio remote --agent {{agent_name}} test`
