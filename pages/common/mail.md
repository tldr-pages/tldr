# mail

> The command operates on the user's mailbox if no argument is given.
> To send an email the message body is built from standard input.

- Send a typed email message. The commandline below continues after pressing Enter key. Input CC email-id (optional) press Enter key. Input message text (can be multi-line). Press "Ctrl-D" key to complete the message text:

`mail -s{{"subject line"}} {{to_user@example.com}}`

- Send email that contains file content:

`mail -s {{"$HOSTNAME filename.txt"}} {{to_user@example.com}} <{{filename.txt}}`

- Send email that contains command output:

`cat {{filename.txt}} | mail -s {{"$HOSTNAME filename.txt"}} {{to_user@example.com}}`

- Send email after an end of long running process:

`{{command}} ; echo {{"job done"}} | mail -s{{"job done"}} {{to_user@example.com}}`

- Send email at the end of shell script:

`notifyemail() { echo "$*" | mail -s {{"$*"}} {{to_user@example.com; }}}`

- Send SMS remainder after 15 minutes:

`echo 'mail -s {{"Call your wife" 13125551234@mobile_carrier.net}}' | at now+15min`

- Send tar.gz file as an attachment:

`tar cvzf - {{directory1 directory2}} | uuencode {{data.tar.gz}} | mail -s {{data}} {{to_user@example.com}}`
