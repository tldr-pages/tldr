# vcluster

> Ստեղծեք և կառավարեք թեթև վիրտուալ Kubernetes կլաստերները անունների տարածքներում:.
> Լրացուցիչ տեղեկություններ. <https://www.vcluster.com/docs/vcluster>:.

- Ստեղծեք վիրտուալ կլաստեր որոշակի անվանատարածքում.:

`vcluster create {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`

- Միացեք վիրտուալ կլաստերին տեղական պորտով և անապահով ռեժիմով.:

`vcluster connect {{vcluster_name}} {{[-n|--namespace]}} {{namespace}} --local-port {{port}} --insecure`

- Թվարկեք բոլոր վիրտուալ կլաստերները.:

`vcluster list`

- Ջնջել վիրտուալ կլաստերը.:

`vcluster delete {{vcluster_name}}`

- Թվարկեք հարթակի կողմից կառավարվող վիրտուալ կլաստերները.:

`vcluster platform list`

- Ստեղծեք հարթակի կողմից կառավարվող վիրտուալ կլաստեր.:

`vcluster platform create {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`

- Միացեք հարթակի կողմից կառավարվող վիրտուալ կլաստերին.:

`vcluster platform connect {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`

- Ջնջել հարթակի կողմից կառավարվող վիրտուալ կլաստերը.:

`vcluster platform delete {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`
