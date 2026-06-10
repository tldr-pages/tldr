# doctl kubernetes կլաստեր

> Կառավարեք Kubernetes կլաստերները և դիտեք կլաստերների հետ կապված կազմաձևման ընտրանքները:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>:.

- Ստեղծեք Kubernetes կլաստեր.:

`doctl {{[k|kubernetes]}} {{[c|cluster]}} {{[c|create]}} --count {{3}} --region {{nyc1}} --size {{s-1vcpu-2gb}} --version {{latest}} {{cluster_name}}`

- Թվարկեք բոլոր Kubernetes կլաստերները.:

`doctl {{[k|kubernetes]}} {{[c|cluster]}} {{[ls|list]}}`

- Վերցրեք և պահպանեք kubeconfig-ը.:

`doctl {{[k|kubernetes]}} {{[c|cluster]}} {{[cfg|kubeconfig]}} {{[s|save]}} {{cluster_name}}`

- Ստուգեք առկա թարմացումների համար.:

`doctl {{[k|kubernetes]}} {{[c|cluster]}} {{[gu|get-upgrades]}} {{cluster_name}}`

- Թարմացրեք կլաստերը նոր Kubernetes տարբերակի.:

`doctl {{[k|kubernetes]}} {{[c|cluster]}} upgrade {{cluster_name}}`

- Ջնջել կլաստերը.:

`doctl {{[k|kubernetes]}} {{[c|cluster]}} {{[d|delete]}} {{cluster_name}}`
