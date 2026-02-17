# openclaw

> A personal AI assistant that you run on your own devices.
> Some subcommands such as `onboard`, `agent`, `doctor`, etc have their own usage documentation.
> More information: <https://github.com/openclaw/openclaw>.

- Run the onboarding wizard to set up the gateway and channels:

`openclaw onboard --install-daemon`

- Start the gateway server:

`openclaw gateway --allow-unconfigured --port {{18789}} --verbose`

- Send a message to a contact:

`openclaw message send {{[-t|--target]}} {{+1234567890}} {{[-m|--message]}} "{{Hello}}"`

- Talk to the assistant with a single message:

`openclaw agent {{[-m|--message]}} "{{Ship checklist}}"`

- Start interactive chat mode:

`openclaw agent`

- Run diagnostics and check system health:

`openclaw doctor`

- Update OpenClaw to the latest version:

`openclaw update`

- List configured channels:

`openclaw channels list`
