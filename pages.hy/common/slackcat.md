# slackcat

> Կոմունալ ֆայլեր փոխանցելու և հրամանի թողարկում Slack-ին:.
> Լրացուցիչ տեղեկություններ. <https://github.com/bcicen/slackcat#usage>:.

- Տեղադրեք ֆայլ Slack-ում.:

`slackcat {{[-c|--channel]}} {{channel_name}} {{path/to/file}}`

- Տեղադրեք ֆայլ Slack-ում հատուկ ֆայլի անունով.:

`slackcat {{[-c|--channel]}} {{channel_name}} {{[-n|--filename]}} {{filename}} {{path/to/file}}`

- Խողովակի հրամանի ելքը Slack-ին որպես տեքստի հատված.:

`{{command}} | slackcat {{[-c|--channel]}} {{channel_name}} {{[-n|--filename]}} {{snippet_name}}`

- Անընդհատ փոխանցեք հրամանի ելքը դեպի Slack.:

`{{command}} | slackcat {{[-c|--channel]}} {{channel_name}} {{[-s|--stream]}}`
