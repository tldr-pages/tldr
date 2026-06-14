# docker buildx du

> Տես սկավառակի օգտագործումը շինարարի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/buildx/du/>:.

- Ցույց տալ սկավառակի օգտագործումը.:

`docker buildx du`

- Զտիչի ելքը՝ հիմնված կոնկրետ պայմանի վրա.:

`docker buildx du --filter "{{description~=golang}}"`

- Ցույց տալ մանրամասն ելքը.:

`docker buildx du --verbose`

- Ձևաչափեք ելքը՝ օգտագործելով Go ձևանմուշը.:

`docker buildx du --format "table {{.ID}}    {{.Description}}"`

- Գեղեցիկ տպագրություն որպես JSON՝ `jq` հրամանով.:

`docker buildx du --format json | jq .`

- Ստուգեք որոշակի շինարարի սկավառակի օգտագործումը.:

`docker buildx du --builder {{builder_name}}`
