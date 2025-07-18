# gemini

> Gemini CLI - Launch an interactive CLI, use -p/--prompt for non-interactive mode.
> More information: <https://github.com/google-gemini/gemini-cli>.

- Start a REPL session to chat interactively:

`gemini`

- Send a prompt and exit immediately (read from stdin):

`echo "{{Summarize the history of Rome}}" | gemini -p`

- Override the default model (default: gemini-2.5-pro):

`gemini -m {{gemini-2.5-flash}}`

- Run inside a sandbox container:

`gemini {{[-s|--sandbox]}}`

- Execute a prompt then stay in interactive mode:

`gemini -i "{{Give me an example of recursion in Python}}"`

- Include all files in context:

`gemini --all-files`

- Show memory usage in status bar:

`gemini --show-memory-usage`
