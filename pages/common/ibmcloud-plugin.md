# ibmcloud plugin

> Manage plugins and plugin repositories for the IBM Cloud CLI.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-plug-ins>.

- List all installed plugins:

`ibmcloud plugin list`

- Install a plugin from a repository:

`ibmcloud plugin install {{plugin_name}}`

- Uninstall a plugin:

`ibmcloud plugin uninstall {{plugin_name}}`

- Update all plugins:

`ibmcloud plugin update --all`

- List available plugins in repositories:

`ibmcloud plugin repo-plugins`

- Add a plugin repository:

`ibmcloud plugin repo-add {{repo_name}} {{repo_url}}`
