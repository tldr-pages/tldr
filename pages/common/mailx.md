# mailx

> Send and receive mail.

- To send mail, the content is typed after the command and ended with Control-D:

`mailx -s "{{subject}}" {{to_addr}}`

- Send mail with short content:

`echo "{{content}}" | mailx -s "{{subject}}" {{to_addr}}`

- Send mail with content which written in a file:

`mailx -s "{{subject}}" {{to_addr}} < {{content.txt}}`

- Send mail to a recipient and CC to another address:

`mailx -s "{{subject}}" -c {{cc_addr}} {{to_addr}}`

- Send mail and set sender address:

`mailx -s "{{subject}}" -r {{from_addr}} {{to_addr}}`

- Send mail with an attachment:

`mailx -a {{file}} -s "{{subject}}" {{to_addr}}`
