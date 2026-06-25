# sfdk deploy

> Deploy build results to a device.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/50-testing-mb2/doc/command.deploy.adoc>.

- Deploy using a specified method:

`sfdk deploy --{{pkcon|rsync|sdk|zypper|zypper-dup|manual}}`

- Preview deploy without applying the changes:

`sfdk deploy --{{method}} {{[-n|--dry-run]}}`

- Deploy files in glob pattern `package*`:

`sfdk deploy --{{method}} "+package*"`

- Deploy all files excluding `ignore*`:

`sfdk deploy --{{method}} "-ignore*"`

- Undeploy using a specified method:

`sfdk undeploy --{{pkcon|rpm|rsync|sdk|zypper}}`
