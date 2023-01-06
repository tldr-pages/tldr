# cs install

> Install an application in the installation directory onfigured when installing `cs`  (to enable the binary to be loaded add to your `.bash_profile` the `$ eval "$(cs install --env)"` command).
> More information: <https://get-coursier.io/docs/cli-install>.

- Install an application:

`cs install {{application-name}}`

- Install a specific version of an application:

`cs install {{application-name}}:{{application-version}}`

- Search an application by a specific name:

`cs search {{application_partial_name}}`

- Update a specific application if available:

`cs update {{application_name}}`

- Update all the installed applications:

`cs update`

- Uninstall an application:

`cs uninstall {{application-name}}`

- List all installed applications:

`cs list`

- Pass a java option to an installed application:

`{{application-name}} -J{{java-option-name}}={{java-option-value}}`
