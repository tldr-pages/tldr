# rvm

> 여러 루비 환경을 쉽게 설치하고 관리하며 작업할 수 있는 도구.
> 더 많은 정보: <https://rvm.io/rvm/cli>.

- 하나 이상의 루비 버전 설치:

`rvm install {{버전1 버전2 ...}}`

- 설치된 버전 목록 표시:

`rvm list`

- 특정 루비 버전 사용:

`rvm use {{버전}}`

- 기본 루비 버전 설정:

`rvm --default use {{버전}}`

- 루비 버전을 새 버전으로 업그레이드:

`rvm upgrade {{현재_버전}} {{새로운_버전}}`

- 루비 버전을 제거하고 소스는 유지:

`rvm uninstall {{버전}}`

- 루비 버전과 소스를 모두 제거:

`rvm remove {{버전}}`

- 운영 체제에 대한 특정 의존성 표시:

`rvm requirements`
