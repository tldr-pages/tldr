# nvm

> Node.js 버전 설치, 제거 또는 전환.
> 버전 번호는 "12.8" 또는 "v16.13.1"과 같이 지정되며, "stable", "system" 등의 라벨을 지원합니다.
> 더 많은 정보: <https://github.com/coreybutler/nvm-windows>.

- Node.js의 특정 버전 설치:

`nvm install {{node_버전}}`

- Node.js의 기본 버전을 설정 (반드시 관리자 권한으로 실행):

`nvm use {{node_버전}}`

- 사용 가능한 모든 Node.js 버전 나열 및 기본 버전 강조:

`nvm list`

- 모든 원격 Node.js 버전 나열:

`nvm ls-remote`

- 지정된 Node.js 버전 제거:

`nvm uninstall {{node_버전}}`
