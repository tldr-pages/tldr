# ng config

> Use JSON path notation (camelCase) to edit workspace or project configurations, such as build options.
> More information: <https://angular.dev/cli/config>.

- Display all configuration values:

`ng config`

- Get a specific configuration value:

`ng config projects.{{app_name}}.prefix`

- Set a configuration value:

`ng config projects.{{app_name}}.prefix {{value}}`

- Disable CLI analytics globally:

`ng config cli.analytics disabled --global`

- Set a global config value(caution: this affects all Angular projects):

`ng config projects.{{app_name}}.prefix {{value}} --global`
