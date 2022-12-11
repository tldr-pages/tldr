# msg

> Send a message to a specific user or session.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- Send a message to a specified user or session:

`msg {{username|session_name|session_id}} {{message}}`

- Send a message from `stdin`:

`echo "{{message}}" | msg {{username|session_name|session_id}}`

- Send a message to a specific server:

`msg /server:{{server_name}} {{username|session_name|session_id}}`

- Send a message to all users of the current machine:

`msg *`

- Set a delay in seconds for a message:

`msg /time:{{seconds}}`
