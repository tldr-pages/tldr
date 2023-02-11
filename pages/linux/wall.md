# wall

> Write a message on the terminals of users currently logged in.
> More information: <https://manned.org/wall>.

- Send a message:

`wall {{message}}`

- Send a message to users that belong to a specific group:

`wall --group {{group_name}} {{message}}`

- Send a message from a file:

`wall {{file}}`

- Send a message with timeout (default 300):

`wall --timeout {{seconds}} {{file}}`
