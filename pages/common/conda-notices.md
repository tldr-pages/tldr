# conda notices

> Retrieve latest channel notifications.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/notices.html#>.

- Show notices for the default channel and all `.condarc` channels:

`conda notices`

- Include a specific channel:

`conda notices {{[-c|--channel]}} {{channel_name}}`

- Ignore default and `.condarc` channels. Requires -c flag:

`conda notices --override-channels -c {{channel_name}}`
