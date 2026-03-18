# apptainer registry

> Manage authentication to OCI/Docker registries.
> See also: `apptainer pull`, `apptainer push`.
> More information: <https://apptainer.org/docs/user/main/cli/apptainer_registry.html>.

- List all configured registry credentials:

`apptainer registry list`

- Log in to a registry with a username (password will be prompted):

`apptainer registry login {{[-u|--username]}} {{username}} docker://{{registry}}`

- Log in to a custom OCI registry:

`apptainer registry login {{[-u|--username]}} {{username}} oras://{{registry}}`

- Log in with username and password:

`apptainer registry login {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} docker://{{registry}}`

- Log in with a password from `stdin`:

`echo "{{password}}" | apptainer registry login {{[-u|--username]}} {{username}} --password-stdin docker://{{registry}}`

- Log in using a custom authentication file:

`apptainer registry login --authfile {{path/to/auth.json}} {{[-u|--username]}} {{username}} docker://{{registry}}`

- Log out from a registry:

`apptainer registry logout docker://{{registry}}`

- Log out using a custom authentication file:

`apptainer registry logout --authfile {{path/to/auth.json}} docker://{{registry}}`
