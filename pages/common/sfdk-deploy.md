# sfdk deploy

> Deploys build results to a device.
> More information: <https://docs.sailfishos.org/Develop/Apps/Tutorials/Building_packages_-_advanced_techniques/>.

- Deploy using a specified method (`pkcon`, `rsync`, `sdk`, `zypper`, `zypper-dup` or `manual`):

`sfdk deploy --{{method}}`

- Preview deploy without applying the changes:

`sfdk deploy --{{method}} --dry-run`

- Deploy files in glob pattern `package*`:

`sfdk deploy --{{method}} "+package*"`

- Deploy all files excluding `ignore*`:

`sfdk deploy --{{method}} "-ignore*"`

- Undeploy using a specified method (`pkcon`, `rpm`, `rsync`, `sdk` or `zypper`):

`sfdk undeploy --{{method}}`
