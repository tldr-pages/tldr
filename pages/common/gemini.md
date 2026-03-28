# gemini

> Launch an interactive prompt with Gemini AI.
> More information: <https://github.com/google-gemini/gemini-cli>.

- Start a REPL session to chat interactively:

`gemini`

- Send the output of another command to Gemini and exit immediately:

`{{echo "Summarize the history of Rome"}} | gemini {{[-p|--prompt]}}`

- Override the default model (default: auto-gemini-3):

`gemini {{[-m|--model]}} {{gemini-3-flash-preview}}`

- Run inside a sandbox container:

`gemini {{[-s|--sandbox]}}`

- Execute a prompt then stay in interactive mode:

`gemini {{[-i|--prompt-interactive]}} "{{Give me an example of recursion in Python}}"`

- Set the approval mode for tool calls:

`gemini {{--approval-mode}} {{[default|auto_edit|yolo|plan]}}`
