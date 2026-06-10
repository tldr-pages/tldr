# kubectl կցել

> Կցեք գործընթացին, որն արդեն աշխատում է գոյություն ունեցող կոնտեյների ներսում:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_attach/>:.

- Ստացեք ելք պատիճից.:

`kubectl attach {{pod_name}}`

- Ստացեք ելք նշված պատիճում գտնվող կոնտեյներից.:

`kubectl attach {{pod_name}} {{[-c|--container]}} {{container_name}}`

- Ստացեք ելք կրկնօրինակների հավաքածուի առաջին պատյանից.:

`kubectl attach {{[rs|replicaset]}}/{{replicaset_name}}`

- Ստեղծեք ինտերակտիվ նիստ պատիճով.:

`kubectl attach {{pod_name}} {{[-it|--stdin --tty]}}`

- Ստեղծեք ինտերակտիվ նստաշրջան հատուկ կոնտեյներով պատիճից.:

`kubectl attach {{pod_name}} {{[-c|--container]}} {{container_name}} {{[-it|--stdin --tty]}}`
