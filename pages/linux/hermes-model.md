# hermes model

> Select the default model and provider for Hermes Agent.
> More information: <https://hermes-agent.nousresearch.com/docs>.

- Interactively select a default model:

`hermes model`

- Override the model for a single invocation:

`hermes -z -m anthropic/claude-sonnet-4.6 "Hello"`

- Override the provider for a single invocation:

`hermes -z --provider openrouter "Hello"`
