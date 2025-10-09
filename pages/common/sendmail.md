# sendmail

> Send email.
> More information: <https://manned.org/sendmail>.

- Send a message with the content of `message.txt` to the mail directory of local user `username`:

`sendmail < {{message.txt}} {{username}}`

- Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the message in `message.txt`:

`sendmail < {{message.txt}} -f {{you@yourdomain.com}} {{test@gmail.com}}`

- Send an email from you@yourdomain.com (assuming the mail server is configured for this) to test@gmail.com containing the file `file.zip`:

`sendmail < {{file.zip}} -f {{you@yourdomain.com}} {{test@gmail.com}}`
