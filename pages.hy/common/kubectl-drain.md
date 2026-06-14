# kubectl արտահոսք

> Սպասարկման նախապատրաստման համար ցամաքեցնել հանգույցը` նշելով այն չպլանավորված և դուրս հանելով բոլոր պատյանները:.
> Տես նաև՝ `kubectl cordon`, `kubectl uncordon`:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/>:.

- Խտացրեք հանգույցը.:

`kubectl drain {{node_name}}`

- Դարձրեք հանգույցը՝ անտեսելով DaemonSet-ի կողմից կառավարվող պատյանները.:

`kubectl drain {{node_name}} --ignore-daemonsets`

- Ջնջեք հանգույցը և ջնջեք պատյանները՝ օգտագործելով դատարկDir ծավալները (տեղական տվյալները կկորչեն).:

`kubectl drain {{node_name}} --ignore-daemonsets --delete-emptydir-data`

- Դարձրեք հանգույցը՝ ստիպելով վտարել հսկիչի կողմից չկառավարվող պատյանները.:

`kubectl drain {{node_name}} --force`

- Խտացրեք հանգույցը, որն ունի հատուկ արտոնյալ ժամկետ՝ պատիճը դադարեցնելու համար.:

`kubectl drain {{node_name}} --grace-period {{seconds}}`

- Դարձրեք հանգույցը՝ վտարելով միայն պիտակների ընտրիչին համապատասխանող պատյանները.:

`kubectl drain {{node_name}} --pod-selector {{label_key}}={{label_value}}`

- Թայմաուտով հանգույցի հեռացում.:

`kubectl drain {{node_name}} --timeout {{duration}}`

- Նախադիտեք ջրահեռացման աշխատանքը՝ առանց փոսերը փաստացի դուրս հանելու (չոր վազք).:

`kubectl drain {{node_name}} --dry-run={{none|server|client}}`
