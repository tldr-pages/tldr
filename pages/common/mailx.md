# mailx

> Send and receive mail.
> More information: <https://manned.org/mailx>.

- Send mail (the content should be typed after the command, and ended with `<Ctrl d>`):

`mailx {{[-s|--subject]}} "{{subject}}" {{to_addr}}`

- Send mail with content passed from another command:

`echo "{{content}}" | mailx {{[-s|--subject]}} "{{subject}}" {{to_addr}}`

- Send mail with content read from a file:

`mailx {{[-s|--subject]}} "{{subject}}" {{to_addr}} < {{content.txt}}`

- Send mail to a recipient and CC to another address:

`mailx {{[-s|--subject]}} "{{subject}}" {{[-c|--cc]}} {{cc_addr}} {{to_addr}}`

- Send mail specifying the sender address:

`mailx {{[-s|--subject]}} "{{subject}}" {{[-r|--from-address]}} {{from_addr}} {{to_addr}}`

- Send mail with an attachment:

`mailx {{[-a|--attach]}} {{path/to/file}} {{[-s|--subject]}} "{{subject}}" {{to_addr}}`
