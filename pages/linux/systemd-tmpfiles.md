# systemd-tmpfiles

> Create, delete, and clean up volatile and temporary files and directories.
> This command is automatically invoked on boot by systemd services and running it manually is usually not needed.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-tmpfiles.html>.

- Create files and directories as specified in the configuration:

`sudo systemd-tmpfiles --create`

- Create files and directories matching only a specific path prefix:

`sudo systemd-tmpfiles --create --prefix {{/var/log/journal}}`

- Clean up files and directories with age parameters configured:

`sudo systemd-tmpfiles --clean`

- Remove files and directories as specified in the configuration:

`sudo systemd-tmpfiles --remove`

- Apply operations for user-specific configurations:

`sudo systemd-tmpfiles --create --user`

- Execute lines marked for early boot:

`sudo systemd-tmpfiles --create --boot`
