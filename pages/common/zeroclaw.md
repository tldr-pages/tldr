# zeroclaw

> Fast, small, and fully autonomous AI assistant infrastructure.
> Some subcommands such as `onboard`, `models`, `service`, etc have their own usage documentation.
> See also: `openclaw`.
> More information: <https://github.com/zeroclaw-labs/zeroclaw#quick-start>.

- Initialize workspace and configuration (quick setup):

`zeroclaw onboard --api-key {{api_key}} --provider {{openrouter|anthropic|openai|...}}`

- Run the full interactive onboarding wizard:

`zeroclaw onboard --interactive`

- Send a single message to the AI agent:

`zeroclaw agent {{[-m|--message]}} "{{Hello, ZeroClaw!}}"`

- Start interactive chat mode:

`zeroclaw agent`

- Start the gateway server (default: 127.0.0.1:8080):

`zeroclaw gateway`

- Start full autonomous runtime (gateway + channels + heartbeat):

`zeroclaw daemon`

- Check system status:

`zeroclaw status`

- Run diagnostics:

`zeroclaw doctor`
