# flux bootstrap

> Kubernetes 클러스터에 Flux를 부트스트랩.
> 더 많은 정보: <https://fluxcd.io/flux/cmd/flux_bootstrap/>.

- GitHub 저장소를 사용하여 Flux 부트스트랩 수행:

`flux bootstrap github --owner {{owner}} --repository {{저장소}} --path {{경로/대상/클러스터_디렉터리}} --personal`

- GitLab 저장소를 사용하여 Flux 부트스트랩 수행:

`flux bootstrap gitlab --owner {{owner}} --repository {{저장소}} --path {{경로/대상/클러스터_디렉터리}}`

- SSH를 통해 일반 Git 저장소를 사용하여 Flux 부트스트랩 수행:

`flux bootstrap git --url {{ssh://git@example.com/repository.git}} --branch {{main}} --path {{경로/대상/클러스터_디렉터리}}`
