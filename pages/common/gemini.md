# gemini

> Launch an interactive prompt with Gemini AI.
> More information: <https://github.com/google-gemini/gemini-cli>.

- Start a REPL session to chat interactively:

`gemini`

- Send the output of another command to Gemini and exit immediately:

`{{echo "Summarize the history of Rome"}} | gemini {{[-p|--prompt]}}`

- Override the default model (default: gemini-2.5-pro):

`gemini {{[-m|--model]}} {{gemini-2.5-flash}}`

- Run inside a sandbox container:

`gemini {{[-s|--sandbox]}}`

- Execute a prompt then stay in interactive mode:

`gemini {{[-i|--prompt-interactive]}} "{{Give me an example of recursion in Python}}"`

- Include all files in context:

`gemini {{[-a|--all-files]}}`

- Show memory usage in status bar:

`gemini --show-memory-usage`
