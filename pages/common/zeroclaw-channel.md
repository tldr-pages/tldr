# zeroclaw channel

> Manage channels (Telegram, Discord, Slack, etc.) for ZeroClaw.
> More information: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- List all configured channels:

`zeroclaw channel list`

- Start all configured channels:

`zeroclaw channel start`

- Run health checks for configured channels:

`zeroclaw channel doctor`

- Add a new channel:

`zeroclaw channel add {{telegram|discord|whatsapp|slack|webhook|...}} '{{json_config}}'`

- Remove a channel:

`zeroclaw channel remove {{channel_name}}`

- View help:

`zeroclaw channel {{[-h|--help]}}`
