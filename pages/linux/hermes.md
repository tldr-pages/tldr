# hermes

> AI assistant CLI with tool-calling, skills, cron jobs, and multi-platform messaging.
> More information: <https://hermes-agent.nousresearch.com/docs>.

- Start interactive chat:

`hermes`

- Send a one-shot prompt and get only the response text (no banner, no spinner):

`hermes -z "What is the weather today?"`

- Resume the most recent session:

`hermes -c`

- Resume a session by name:

`hermes -c "my project"`

- Preload skills for the session:

`hermes -s github,hermes-agent`

- Launch the modern TUI:

`hermes --tui`

- Force the classic CLI:

`hermes --cli`

- Build and launch the native desktop app:

`hermes desktop`
