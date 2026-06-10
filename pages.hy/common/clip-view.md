# հոլովակի դիտում

> Command Line Interface Pages (CLIP) մատուցում:.
> Render TlDr-ի նմանվող նախագծի համար՝ շատ ավելի ընդարձակ շարահյուսությամբ և մի քանի արտապատկերման ռեժիմներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/command-line-interface-pages/v2-tooling/tree/main/clip-view>:.

- Ներկայացրեք հատուկ տեղական էջեր.:

`clip-view {{path/to/page1.clip path/to/page2.clip ...}}`

- Ներկայացրեք որոշակի հեռավոր էջեր.:

`clip-view {{page_name1 page_name2 ...}}`

- Ներկայացրեք էջերը հատուկ մատուցման միջոցով.:

`clip-view --render {{tldr|tldr-colorful|docopt|docopt-colorful}} {{page_name1 page_name2 ...}}`

- Ներկայացրեք էջերը հատուկ գունային թեմայով.:

`clip-view --theme {{path/to/local_theme.yaml|remote_theme_name}} {{page_name1 page_name2 ...}}`

- Մաքրել էջի կամ թեմայի քեշը.:

`clip-view --clear-{{page|theme}}-cache`

- Ցուցադրել օգնությունը.:

`clip-view --help`

- Ցուցադրման տարբերակը:

`clip-view --version`
