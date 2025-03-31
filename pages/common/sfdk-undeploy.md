# sfdk undeploy

> Undeploys build results from a device.

- Undeploy using a specified method (`pkcon`, `rpm`, `rsync`, `sdk` or `zypper`):

`sfdk undeploy --{{method}}`

- Preview undeploy without applying the changes:

`sfdk undeploy --{{method}} --dry-run`

- Undeploy files in glob pattern `package*`:

`sfdk undeploy --{{method}} "+package*"`

- Undeploy all files excluding `ignore*`:

`sfdk undeploy --{{method}} "-ignore*"`
