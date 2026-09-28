# llm keys

> Manage stored API keys for different models.
> More information: <https://llm.datasette.io/en/stable/help.html#llm-keys-help>.

- List the names of all stored keys:

`llm keys list`

- Save an API key for a model provider (prompts for the key):

`llm keys set {{openai}}`

- Print the value of a stored key:

`llm keys get {{openai}}`

- Print the path to the `keys.json` file where keys are stored:

`llm keys path`
