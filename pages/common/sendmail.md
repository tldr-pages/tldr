# sendmail

> Send email from the command line.

- Send a message with the content of message.txt to the mail folder of local user `user_name`:

`sendmail user_name < message.txt`

- Send an email from you@yourdomain.com (assuming your local mail server is configured for this) to test@gmail.com containing the message in `message.txt`:

`sendmail -f test@gmail.com you@yourdomain.com < message.txt`

- Send an email from you@yourdomain.com (assuming your local mail server is configured for this) to test@gmail.com containing the file `file.zip`:

`sendmail -f test@gmail.com you@yourdomain.com < file.zip`
