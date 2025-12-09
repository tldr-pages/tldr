# ntfyme

> A notification tool to track and notify you about your long-running termination process.
> Send notifications with success/error messages with Gmail, Telegram, and more.
> More information: <https://github.com/AnirudhG07/ntfyme>.

- Directly run your command:

`ntfyme exec {{[-c|--cmd]}} {{command}}`

- Pipe your command and run:

`echo {{command}} | ntfyme exec`

- Run multiple commands by enclosing them in quotes:

`echo "{{command1; command2; command3}}" | ntfyme exec`

- Track and terminate the process after prolonged suspension:

`ntfyme exec {{[-t|--track-process]}} {{[-c|--cmd]}} {{command}}`

- Setup the tool configurations interactively:

`ntfyme setup`

- Encrypt your password:

`ntfyme enc`

- See the log history:

`ntfyme log`

- Open and edit the configuration file:

`ntfyme config`
