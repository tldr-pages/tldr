# flux create

> Flux 리소스를 생성하거나 업데이트.
> 더 많은 정보: <https://fluxcd.io/flux/cmd/flux_create/>.

- GitRepository 소스 생성:

`flux create source git {{소스_이름}} --url {{https://github.com/repository}} --branch {{브랜치_이름}}`

- Git 소스의 디렉터리를 동기화하는 Kustomization 리소스 생성:

`flux create kustomization {{kustomization_이름}} --source {{소스_이름}} --path {{경로/대상/디렉터리}}`

- HelmRelease 생성:

`flux create helmrelease {{릴리스_이름}} --chart {{차트_이름}} --source {{HelmRepository/저장소_이름}}`

- Git 저장소 인증을 위한 Secret 생성:

`flux create secret git {{비밀_이름}} --url {{https://github.com/repository}} --username "{{사용자명}}" --password "{{비밀번호}}"`
