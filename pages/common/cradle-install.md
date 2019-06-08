# cradle install

> Installs the Cradle PHP framework components.
> More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Install Cradle's components (User will be prompted for further details):

`cradle install`

- Forcefully overwrite files:

`cradle install --force`

- Skip running SQL migrations:

`cradle install --skip-sql`

- Skip running package updates:

`cradle install --skip-versioning`

- Use specific database details:

`cradle install -h {{hostname}} -u {{username}} -p {{password}}`
