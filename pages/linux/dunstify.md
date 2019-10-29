# dunstify

> A notification tool that is an extension of notify-send, but has more features based around dunst
> Works with all options that work for notify-send

- Show a notification with title "Title" and message "Message"

`dunstify {{"Title"}} {{"Message"}}`

- Show a notification with specified urgency (options: "low", "normal", "high")

`dunstify {{"Title"}} {{"Message}}" -u high

- Show a message with a message ID of 123 (will overwrite previous messages with the same ID)

`dunstify {{"Title"}} {{"Message"}} -r 123
