# choco apikey

> Manage API keys for Chocolatey sources.
> More information: <https://chocolatey.org/docs/commands-apikey>.

- Display a list of sources and their API keys:

`choco apikey`

- Display a specific source and its API key:

`choco apikey {{[-s|--source]}} "{{source_url}}"`

- Set an API key for a source:

`choco apikey {{[-s|--source]}} "{{source_url}}" {{[-k|--api-key]}} "{{api_key}}"`

- Remove an API key for a source:

`choco apikey {{[-s|--source]}} "{{source_url}}" --remove`
