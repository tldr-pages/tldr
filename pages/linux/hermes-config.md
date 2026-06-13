# hermes config

> View and edit the Hermes configuration file.
> More information: <https://hermes-agent.nousresearch.com/docs>.

- View the current configuration:

`hermes config`

- Edit the configuration in your `$EDITOR`:

`hermes config edit`

- Set a configuration value:

`hermes config set {{key}} {{value}}`

- Set the default model provider:

`hermes config set model.provider openrouter`

- Set the default model name:

`hermes config set model.name anthropic/claude-sonnet-4.6`

- List all configuration keys and values:

`hermes config list`
