# flux build

> Flux 매니페스트를 생성.
> 더 많은 정보: <https://fluxcd.io/flux/cmd/flux_build/>.

- Kustomization 매니페스트 생성:

`flux build kustomization {{이름}} --path {{경로/대상/kustomization}}`

- Kustomization 매니페스트를 생성하여 파일로 저장:

`flux build kustomization {{이름}} --path {{경로/대상/kustomization}} > {{경로/대상/manifests.yaml}}`

- Kustomization 매니페스트를 생성하고 `kubectl`에 직접 전달하여 적용:

`flux build kustomization {{이름}} --path {{경로/대상/kustomization}} | kubectl apply -f -`
