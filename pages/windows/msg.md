# msg

> Send a message to a specific user or session.

- Send a message to a specified user or session:

`msg {{username|session_name|session_id}} {{message}}`

- Send a message from stdin:

`echo "{{message}}" | msg`

- Send a message to a specific server:

`msg /server:{{server_name}}`

- Set a delay in seconds for a message:

`msg /time:{{seconds}}`
