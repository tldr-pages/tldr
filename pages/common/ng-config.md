# ng config

> Retrieve or set Angular workspace configuration values in `angular.json`.
> More information: <https://angular.dev/cli/config>.

- Display all configuration values:

`ng config`

- Get a specific configuration value:

`ng config projects.{{app_name}}.prefix`

- Set a configuration value:

`ng config projects.{{app_name}}.prefix {{value}}`

- Disable CLI analytics globally:

`ng config cli.analytics disabled --global`
