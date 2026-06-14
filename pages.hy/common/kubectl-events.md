# kubectl իրադարձություններ

> Ցուցադրել ռեսուրսների իրադարձությունները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_events/>:.

- Ցույց տալ իրադարձությունները լռելյայն անվանատարածքում.:

`kubectl events`

- Ցույց տալ իրադարձությունները բոլոր անվանատարածքներում.:

`kubectl events {{[-A|--all-namespaces]}}`

- Դիտեք իրադարձությունները որոշակի անվանատարածքում.:

`kubectl events {{[-w|--watch]}} {{[-n|--namespace]}} {{namespace}}`

- Ցուցադրել իրադարձությունները pod-ի համար որոշակի անվանատարածքում.:

`kubectl events --for {{pod}}/{{pod_name}} {{[-n|--namespace]}} {{namespace}}`

- Ցույց տալ իրադարձությունները ռեսուրսի համար որոշակի անվանատարածքում.:

`kubectl events --for {{resource}}/{{resource_name}} {{[-n|--namespace]}} {{namespace}}`

- Ցույց տալ իրադարձությունները `Warning` կամ `Normal` տիպի համար.:

`kubectl events --types Warning,Normal`

- Արդյունք իրադարձություններ YAML ձևաչափով.:

`kubectl events {{[-o|--output]}} yaml`
