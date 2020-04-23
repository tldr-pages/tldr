# dunstify

> A notification tool that is an extension of notify-send, but has more features based around dunst.
> Works with all options that work for notify-send.

- Show a notification with a given title and message:

`dunstify {{"Title"}} {{"Message"}}`

- Show a notification with specified urgency:

`dunstify {{"Title"}} {{"Message}}" -u {{low|normal|critical}}`

- Specify a message ID (overwrites any previous messages with the same ID):

`dunstify {{"Title"}} {{"Message"}} -r {{123}}`

- To see other possible options:

`notify-send --help`
