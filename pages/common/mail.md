# mail

> The command operates on the user's mailbox if no argument is given.
> To send an email the message body is built from standard input.

- Send a typed email message. The command line below continues after pressing Enter key. Input CC email-id (optional) press Enter key. Input message text (can be multi-line). Press Ctrl-D key to complete the message text:

`mail --subject="{{subject line}}" {{to_user@example.com}}`

- Send an email that contains file content:

`mail --subject="{{$HOSTNAME filename.txt}}" {{to_user@example.com}} < {{path/to/filename.txt}}`

- Send a `tar.gz` file as an attachment:

`tar cvzf - {{path/to/directory1 path/to/directory2}} | uuencode {{data.tar.gz}} | mail --subject="{{subject_line}}" {{to_user@example.com}}`
