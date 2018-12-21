# wall

> Write a message on the terminals of users currently logged in.

- Send a message:

`echo "{{message}}" | wall`

- Send a message from a file:

`wall {{file}}`

- Send a message with timeout (default 300):

`wall -t {{seconds}} {{file}}`
