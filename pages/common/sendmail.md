# sendmail

> Send email.
> More information: <https://manned.org/sendmail>.

- Send a message with the content of `message.txt` to the mail directory of local user `username`:

`sendmail < {{message.txt}} {{username}}`

- Send an email from sender@example.com (assuming the mail server is configured for this) to receiver@example.com containing the message in `message.txt`:

`sendmail < message.txt -f sender@example.com receiver@example.com`

- Send an email from sender@example.com (assuming the mail server is configured for this) to receiver@example.com containing the file `file.zip`:

`sendmail < file.zip -f sender@example.com receiver@example.com`
