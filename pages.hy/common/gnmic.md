#gnmic

> GNMI հաճախորդ:.
> Կառավարեք gNMI ցանցային սարքի կազմաձևումը և դիտեք գործառնական տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://gnmic.openconfig.net/user_guide/configuration_flags/>:.

- Պահանջել սարքի հնարավորությունները.:

`gnmic {{[-a|--address]}} {{ip:port}} capabilities`

- Տրամադրեք օգտվողի անուն և գաղտնաբառ՝ սարքի հնարավորությունները ստանալու համար.:

`gnmic {{[-a|--address]}} {{ip:port}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} capabilities`

- Ստացեք սարքի վիճակի պատկերը որոշակի ուղու վրա.:

`gnmic {{[-a|--address]}} {{ip:port}} get --path {{path}}`

- Թարմացրեք սարքի վիճակը որոշակի ճանապարհով.:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- Բաժանորդագրվեք ենթածառի տակ գտնվող թիրախային վիճակի թարմացումներին որոշակի ճանապարհով.:

`gnmic {{[-a|--address]}} {{ip:port}} {{[sub|subscribe]}} --path {{path}}`
