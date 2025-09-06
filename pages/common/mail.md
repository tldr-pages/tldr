# mail

> Operate on the user's mailbox.
> To send an email the message body is built from `stdin`.
> More information: <https://manned.org/mail>.

- Open an interactive prompt to check personal mail:

`mail`

- Send a typed email message with optional CC. The command-line below continues after pressing `<Enter>`. Input message text (can be multiline). Press `<Ctrl d>` to complete the message text:

`mail --subject "{{subject line}}" {{to_user@example.com}} --cc "{{cc_email_address}}"`

- Send an email that contains file content:

`mail --subject "{{$HOSTNAME filename.txt}}" {{to_user@example.com}} < {{path/to/filename.txt}}`

- Send a `tar.gz` file as an attachment:

`tar cvzf - {{path/to/directory1 path/to/directory2}} | uuencode {{data.tar.gz}} | mail --subject "{{subject_line}}" {{to_user@example.com}}`

- Display help:

`mail {{[-h|--help]}}`
