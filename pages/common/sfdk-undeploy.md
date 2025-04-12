# sfdk undeploy

> Undeploys build results from a device.
> More information: <https://docs.sailfishos.org/Tools/Sailfish_SDK/Deploying_packages/>.

- Undeploy using a specified method (`pkcon`, `rpm`, `rsync`, `sdk` or `zypper`):

`sfdk undeploy --{{method}}`

- Preview undeploy without applying the changes:

`sfdk undeploy --{{method}} {{[-n|--dry-run]}}`

- Undeploy files in glob pattern `package*`:

`sfdk undeploy --{{method}} "+package*"`

- Undeploy all files excluding `ignore*`:

`sfdk undeploy --{{method}} "-ignore*"`
