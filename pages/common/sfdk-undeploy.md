# sfdk undeploy

> Undeploys build results from a device.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/50-testing-mb2/doc/command.undeploy.adoc>.

- Undeploy using a specified method (`pkcon`, `rpm`, `rsync`, `sdk` or `zypper`):

`sfdk undeploy --{{method}}`

- Preview undeploy without applying the changes:

`sfdk undeploy --{{method}} {{[-n|--dry-run]}}`

- Undeploy files in glob pattern `package*`:

`sfdk undeploy --{{method}} "+package*"`

- Undeploy all files excluding `ignore*`:

`sfdk undeploy --{{method}} "-ignore*"`
