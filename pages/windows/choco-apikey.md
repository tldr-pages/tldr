# choco-apikey

> Manage API keys for Chocolatey sources.
> More information: <https://docs.chocolatey.org/en-us/create/commands/api-key>.

- Print all sources and their API keys:

`choco apikey`

- Print a specified source and the associated API key:

`choco apikey --source "{{source_url}}"`

- Set an API key for the specified source:

`choco apikey --source "{{source_url}}" --key "{{api_key}}"`

- Remove the API key for the specified source:

`choco apikey --source "{{source_url}}" --remove`
