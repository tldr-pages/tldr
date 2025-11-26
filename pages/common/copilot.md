# copilot

> Interact with GitHub Copilot.
> More information: <https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli>.

- Start interactive mode:

`copilot`

- Allow all file editing:

`copilot --allow-tool write`

- Resume the most recent session:

`copilot --continue`

- Resume a previous session using session picker:

`copilot --resume`

- Use a specific model:

`copilot --model "{{gpt-5}}"`

- Allow all Git commands except `git push`:

`copilot --allow-tool 'shell(git:*)' --deny-tool 'shell(git push)'`

- Execute a prompt directly without interactive mode, while allowing `copilot` to run any command:

`copilot {{[-p|--prompt]}} "{{Fix the bug in main.js}}" --allow-all-tools`
