# wall

> write a message on the terminals of users currently logged in
> only available to super-user

- send a message

`echo "{{message}}" | wall`

- send a message from a file

`wall {{file}}`

- send a message with timeout (default 300)

`wall -t {{seconds}} {{file}}`
