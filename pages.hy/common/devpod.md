# devpod

> Գործարկեք վերարտադրվող զարգացման միջավայրեր՝ օգտագործելով Docker, Kubernetes կամ SSH:.
> Լրացուցիչ տեղեկություններ. <https://devpod.sh/docs/quickstart/devpod-cli/>:.

- Ավելացնել մատակարար, ինչպիսիք են Docker-ը կամ Kubernetes-ը.:

`devpod provider add {{provider_name}}`

- Թվարկեք բոլոր հասանելի մատակարարները.:

`devpod provider list-available`

- Սկսեք աշխատանքային տարածք GitHub-ի պահոցից հատուկ IDE-ով.:

`devpod up {{github.com/user/repo}} {{[-i|--ide]}} {{vscode}}`

- Սկսեք աշխատանքային տարածք տեղական գրացուցակից.:

`devpod up {{path/to/project}}`

- Վերստեղծեք գոյություն ունեցող աշխատանքային տարածք.:

`devpod up {{workspace_name}} {{[-r|--recreate]}}`

- Վերականգնել աշխատանքային տարածքը մաքուր վիճակի.:

`devpod up {{workspace_name}} {{[-x|--reset]}}`

- Ավելացրեք հատուկ մատակարար GitHub պահոցից.:

`devpod provider add {{org/provider-repo}}`
