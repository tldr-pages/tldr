# dunstify

> A notification tool that is an extension of `notify-send`, but has more features based around `dunst`.
> Accepts all options of `notify-send`.
> More information: <https://dunst-project.org/documentation/dunstify>.

- Show a notification with a given title and message:

`dunstify "{{Title}}" "{{Message}}"`

- Show a notification with the specified urgency:

`dunstify "{{Title}}" "{{Message}}" {{[-u|--urgency]}} {{low|normal|critical}}`

- Specify a message ID (overwrites any previous messages with the same ID):

`dunstify "{{Title}}" "{{Message}}" {{[-r|--replace]}} {{123}}`

- Display help:

`dunstify {{[-?|--help]}}`
