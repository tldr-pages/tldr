# zeroclaw agent

> Start the AI agent loop for interacting with ZeroClaw.
> More information: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- Send a single message to the AI agent:

`zeroclaw agent {{[-m|--message]}} "{{Hello, ZeroClaw!}}"`

- Start interactive chat mode:

`zeroclaw agent`

- Send a message with a specific provider:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" {{[-p|--provider]}} {{anthropic}}`

- Send a message with a specific model:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" --model {{anthropic/claude-sonnet-4-20250514}}`

- Send a message with custom temperature:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" {{[-t|--temperature]}} {{0.5}}`

- Send a message and attach a hardware peripheral:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" --peripheral {{nucleo-f401re:/dev/ttyACM0}}`

- Display help:

`zeroclaw agent {{[-h|--help]}}`
