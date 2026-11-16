# flux suspend

> Flux 리소스의 조정(Reconciliation) 작업을 일시 중지.
> 더 많은 정보: <https://fluxcd.io/flux/cmd/flux_suspend/>.

- 지정한 Kustomization의 조정 작업 일시 중지:

`flux suspend kustomization {{kustomization_이름}}`

- 네임스페이스의 모든 Kustomization 조정 작업 일시 중지:

`flux suspend kustomization --all`

- 지정한 HelmRelease의 조정 작업 일시 중지:

`flux suspend helmrelease {{릴리스_이름}}`

- 지정한 GitRepository 소스의 조정 작업 일시 중지:

`flux suspend source git {{소스_이름}}`

- 지정한 ImageUpdateAutomation 리소스의 조정 작업 일시 중지:

`flux suspend image update {{자동화_이름}}`
