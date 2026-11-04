# flux

> Kubernetes를 위한 지속적 및 점진적 배포 솔루션.
> 더 많은 정보: <https://fluxcd.io/flux/cmd/>.

- 클러스터가 Flux의 사전 요구 사항을 충족하는지 확인:

`flux check --pre`

- Kubernetes 클러스터에 Flux 부트스트랩 수행:

`flux bootstrap {{github|gitlab}} --owner {{소유자}} --repository {{레포지토리}} --path {{경로/대상/클러스터_디렉터리}}`

- 새로운 GitRepository 소스 생성:

`flux create source git {{소스_이름}} --url {{https://github.com/repository}} --branch {{브랜치_이름}}`

- 모든 Flux 사용자 정의 리소스 목록 표시:

`flux get all`

- 지정한 Kustomization의 reconciliation을 수행하고 소스의 변경 사항 적용:

`flux reconcile kustomization {{이름}} --with-source`

- Kustomization의 reconciliation 일시 정지:

`flux suspend kustomization {{이름}}`

- Kustomization의 reconciliation 재개:

`flux resume kustomization {{이름}}`

- 지정한 하위 명령어에 대한 도움말 표시:

`flux {{하위_명령어}} --help`
