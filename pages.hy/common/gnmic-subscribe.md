# gnmic բաժանորդագրվել

> Բաժանորդագրվեք gnmic ցանցի սարքի վիճակի թարմացումներին:.
> Լրացուցիչ տեղեկություններ. <https://gnmic.openconfig.net/cmd/subscribe/>:.

- Բաժանորդագրվեք թիրախային վիճակի թարմացումներին որոշակի ուղու ենթածառի տակ.:

`gnmic {{[-a|--address]}} {{ip:port}} {{[sub|subscribe]}} --path {{path}}`

- Բաժանորդագրվեք թիրախին 30 վրկ նմուշի միջակայքով (կանխադրվածը 10 վրկ է).:

`gnmic {{[-a|--address]}} {{ip:port}} {{[sub|subscribe]}} --path {{path}} --sample-interval 30s`

- Բաժանորդագրվեք թիրախին օրինակելի ընդմիջումով և թարմացումներով միայն փոփոխության դեպքում.:

`gnmic {{[-a|--address]}} {{ip:port}} {{[sub|subscribe]}} --path {{path}} --stream-mode on-change --heartbeat-interval {{1m}}`

- Բաժանորդագրվեք թիրախին միայն մեկ թարմացման համար.:

`gnmic {{[-a|--address]}} {{ip:port}} {{[sub|subscribe]}} --path {{path}} --mode once`

- Բաժանորդագրվեք թիրախին և նշեք պատասխանի կոդավորումը (json_ietf):

`gnmic {{[-a|--address]}} {{ip:port}} {{[sub|subscribe]}} --path {{path}} {{[-e|--encoding]}} json_ietf`
