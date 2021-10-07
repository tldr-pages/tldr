# mailx

> Send and receive mail.
> More information: <https://manned.org/mailx>.

- Send mail (the content should be typed after the command, and ended with `Ctrl+D`):

`mailx -s "{{subject}}" {{to_addr}}`

- Send mail with content passed from another command:

`echo "{{content}}" | mailx -s "{{subject}}" {{to_addr}}`

- Send mail with content read from a file:

`mailx -s "{{subject}}" {{to_addr}} < {{content.txt}}`

- Send mail to a recipient and CC to another address:

`mailx -s "{{subject}}" -c {{cc_addr}} {{to_addr}}`

- Send mail specifying the sender address:

`mailx -s "{{subject}}" -r {{from_addr}} {{to_addr}}`

- Send mail with an attachment:

`mailx -a {{file}} -s "{{subject}}" {{to_addr}}`
