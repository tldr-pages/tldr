# npm access

> 게시된 패키지에 대한 접근 수준 설정.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-access>.

- 사용자 또는 범위에 대한 패키지 나열:

`npm access list packages {{사용자|범위|범위:팀}} {{패키지_이름}}`

- 패키지의 공동 작업자 나열:

`npm access list collaborators {{패키지_이름}} {{사용자_명}}`

- 패키지 상태 확인:

`npm access get status {{패키지_이름}}`

- 패키지 상태 설정 (공개 또는 비공개):

`npm access set status {{public|private}} {{패키지_이름}}`

- 패키지에 대한 접근 권한 부여:

`npm access grant {{read-only|read-write}} {{범위:팀}} {{패키지_이름}}`

- 패키지에 대한 접근 권한 철회:

`npm access revoke {{범위:팀}} {{패키지_이름}}`

- 2단계 인증 요구 사항 구성:

`npm access set mfa {{none|publish|automation}} {{패키지_이름}}`
