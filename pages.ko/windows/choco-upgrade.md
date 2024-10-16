# choco upgrade

> Chocolatey로 하나 이상의 패키지를 업그레이드.
> 더 많은 정보: <https://chocolatey.org/docs/commands-upgrade>.

- 하나 이상의 패키지 업그레이드:

`choco upgrade {{패키지1 패키지2 ...}}`

- 특정 버전으로 패키지 업그레이드:

`choco upgrade {{패키지}} --version {{버전}}`

- 모든 패키지 업그레이드:

`choco upgrade all`

- 지정된 쉼표로 구분된 패키지를 제외하고 모든 패키지 업그레이드:

`choco upgrade all --except "{{패키지1,패키지2,...}}"`

- 모든 프롬프트 자동으로 확인:

`choco upgrade {{패키지}} --yes`

- 패키지를 받을 사용자 지정 소스 지정:

`choco upgrade {{패키지}} --source {{소스_주소|별칭}}`

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco upgrade {{패키지}} --user {{사용자_명}} --password {{비밀번호}}`
