# llm keys

> Manage API keys for Large Language Model providers.
> See also: `llm`.
> More information: <https://llm.datasette.io/en/stable/help.html>.

- Set an API key for a provider (prompts for key input):

`llm keys set {{provider_name}}`

- List all stored API key names:

`llm keys list`

- Retrieve the value of a specific key:

`llm keys get {{provider_name}}`

- Display the path to the `keys.json` file:

`llm keys path`

- Display help:

`llm keys --help`
