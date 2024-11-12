# choco uninstall

> Chocolatey를 사용하여 패키지 제거.
> 더 많은 정보: <https://chocolatey.org/docs/commands-uninstall>.

- 하나 이상의 패키지 제거:

`choco uninstall {{패키지1 패키지2 ...}}`

- 특정 버전의 패키지 제거:

`choco uninstall {{패키지}} --version {{버전}}`

- 모든 프롬프트를 자동으로 확인:

`choco uninstall {{패키지}} --yes`

- 제거 시 모든 의존성 제거:

`choco uninstall {{패키지}} --remove-dependencies`

- 모든 패키지 제거:

`choco uninstall all`
