# ntfyme

> A notification tool to track and notify you about your long running process on termination.
> Send notification with Gmail, Telegram and more with success/error messages.
> More information: <https://github.com/AnirudhG07/ntfyme>.

- Directly run your command:

`ntfyme exec {{-c|--cmd}} {{COMMAND}}`

- Pipe your command and run:

`echo {{COMMAND}} | ntfyme exec`

- Run multiple commands by enclosing them in quotes:

`echo "{{COMMAND1; COMMAND2; COMMAND3}}" | ntfyme exec`

- Track and terminate your process after prolong suspension:

`ntfyme exec {{-t|--track-process}} {{-c|--cmd}} {{COMMAND}}`

- Setup the tool configurations interactively:

`ntfyme setup`

- Encrypt your password:

`ntfyme enc`

- See the log history:

`ntfyme log`

- Open and edit the configuration file:

`ntfyme config`
