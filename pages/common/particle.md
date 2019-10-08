# particle

> A command-line tool for interacting with Particle devices.
> More information: <https://docs.particle.io/tutorials/developer-tools/cli>.

- Log in or create an account for the Particle CLI:

`particle setup`

- Display a list of devices:

`particle list`

- Create a new Particle project interactively:

`particle project create`

- Compile a Particle project:

`particle compile {{device_type}} {{path/to/source_code.ino}}`

- Update a device to use a specific app remotely:

`particle flash {{device_name}} {{path/to/program.bin}}`

- Update a device to use the latest firmware via serial:

`particle flash --serial {{path/to/firmware.bin}}`

- Execute a function on a device:

`particle call {{device_name}} {{function_name}} {{function_arguments}}`
