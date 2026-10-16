# flux uninstall

> Flux와 사용자 지정 리소스 정의(CRD)를 제거.
> 더 많은 정보: <https://fluxcd.io/flux/cmd/flux_uninstall/>.

- Flux 컴포넌트, 사용자 지정 리소스 및 네임스페이스 제거:

`flux uninstall`

- 확인 메시지 없이 Flux 제거:

`flux uninstall {{[-s|--silent]}}`

- 지정한 네임스페이스에서 Flux 제거:

`flux uninstall {{[-n|--namespace]}} {{네임스페이스}}`

- 네임스페이스는 유지하고 Flux 제거:

`flux uninstall --keep-namespace`

- Flux를 실제로 제거하지 않고 제거 과정 미리 확인:

`flux uninstall --dry-run`
