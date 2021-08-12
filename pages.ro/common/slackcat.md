# slackcat

> Utilitar pentru transmiterea fișierelor și ieșirea comenzii în Slack.
> Mai multe informaţii: <https://github.com/bcicen/slackcat>

- Postați un fișier la Slack:

`slackcat --channel {{channel_name}} {{path/to/file}}`

- Postați un fișier în Slack cu un nume de fișier personalizat:

`slackcat --channel {{channel_name}} --filename={{filename}} {{path/to/file}}`

- ieșire de comandă țeavă la Slack ca fragment de text:

`{{command}} | slackcat --channel {{channel_name}} --filename={{snippet_name}}`

- Transmite comanda de ieșire la Slack continuu:

`{{command}} | slackcat --channel {{channel_name}} --stream`
