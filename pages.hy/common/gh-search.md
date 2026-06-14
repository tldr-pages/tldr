# gh որոնում

> Որոնել ամբողջ GitHub-ում:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_search>:.

- Որոնեք հատուկ հիմնաբառեր պարունակող կոդը.:

`gh search code {{keyword1 keyword2 ...}}`

- Որոնեք խնդիրներ կոնկրետ արտահայտությամբ.:

`gh search issues "{{search_phrase}}"`

- Որոնման պարտավորություններ կոնկրետ հեղինակի կողմից.:

`gh search commits --author {{username}}`

- Որոնեք ձգողականության հարցումներ, որոնք ձեզ հանձնարարված են, որոնք դեռ բաց են.:

`gh search prs --assignee @me --state open`

- Որոնեք պահեստները կազմակերպությունում ըստ թեմայի.:

`gh search repos --owner {{org_name}} --topic {{topic_name}}`

- Որոնեք խնդիրներ առանց որոշակի պիտակի (Unix-ի նման համակարգեր).:

`gh search issues -- "{{search_query}} -label:{{label_name}}"`

- Որոնեք խնդիրներ առանց որոշակի պիտակի (PowerShell):

`gh --% search issues -- "{{search_query}} -label:{{label_name}}"`

- Բացեք որոնման հարցումը վեբ բրաուզերում.:

`gh search {{subcommand}} {{[-w|--web]}} {{query}}`
