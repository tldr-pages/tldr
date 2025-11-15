# nvm

> fish 셸에서 Node.js 버전을 설치, 제거 또는 전환.
> "12.8" 또는 "v16.13.1"과 같은 버전 번호 및 "stable", "system" 등의 레이블을 지원.
> 더 많은 정보: <https://github.com/jorgebucaran/nvm.fish>.

- 특정 버전의 Node.js 설치:

`nvm install {{노드_버전}}`

- 현재 셸에서 특정 버전의 Node.js 사용:

`nvm use {{노드_버전}}`

- 기본 Node.js 버전 설정:

`set nvm_default_version {{노드_버전}}`

- 사용 가능한 모든 Node.js 버전 나열 및 기본 버전 강조:

`nvm list`

- 지정된 Node.js 버전 제거:

`nvm uninstall {{노드_버전}}`
