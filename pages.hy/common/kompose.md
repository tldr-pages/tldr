#կազմել

> Փոխարկել docker-compose հավելվածները Kubernetes-ի:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kubernetes/kompose>:.

- Տեղադրեք dockerized հավելված Kubernetes-ում.:

`kompose up {{[-f|--file]}} {{docker-compose.yml}}`

- Ջնջել ակնթարթային ծառայությունները/տեղակայումները Kubernetes-ից.:

`kompose down {{[-f|--file]}} {{docker-compose.yml}}`

- Փոխարկեք docker-compose ֆայլը Kubernetes ռեսուրսների ֆայլի.:

`kompose convert {{[-f|--file]}} {{docker-compose.yml}}`
