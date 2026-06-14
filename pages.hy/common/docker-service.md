# դոկեր ծառայություն

> Կառավարեք ծառայությունները Docker daemon-ի վրա:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/service/>:.

- Թվարկեք ծառայությունները Docker daemon-ի վրա.:

`docker service ls`

- Ստեղծեք նոր ծառայություն.:

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- Ցուցադրել մանրամասն տեղեկություններ մեկ կամ մի քանի ծառայությունների մասին.:

`docker service inspect {{service_name_or_id1 service_name_or_id2 ...}}`

- Թվարկեք մեկ կամ մի քանի ծառայությունների առաջադրանքները.:

`docker service ps {{service_name_or_id1 service_name_or_id2 ...}}`

- Տիեզերքով առանձնացված ծառայությունների ցանկի մասշտաբով կրկնօրինակների որոշակի քանակություն.:

`docker service scale {{service_name}}={{count_of_replicas}}`

- Հեռացնել մեկ կամ մի քանի ծառայություններ.:

`docker service rm {{service_name_or_id1 service_name_or_id2 ...}}`
