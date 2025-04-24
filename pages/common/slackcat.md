# slackcat

> Utility for passing files and command output to Slack.
> More information: <https://github.com/bcicen/slackcat>.

- Post a file to Slack:

`slackcat --channel {{channel_name}} {{path/to/file}}`

- Post a file to Slack with a custom filename:

`slackcat --channel {{channel_name}} --filename={{filename}} {{path/to/file}}`

- Pipe command output to Slack as a text snippet:

`{{command}} | slackcat --channel {{channel_name}} --filename={{snippet_name}}`

- Stream command output to Slack continuously:

`{{command}} | slackcat --channel {{channel_name}} --stream`
