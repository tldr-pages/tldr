# ni

> 적절한 패키지 관리자 (npm, yarn, pnpm, bun 또는 deno)를 자동으로 사용함.
> 현재 프로젝트의 lockfile을 감지하여 해당하는 명령어를 실행할 수 있게 함.
> 참고: PowerShell에서, `ni`가 `New-Item`의 기본 별칭. 이 도구를 사용하려면, 해당 별칭을 제거해야 함.
> 더 많은 정보: <https://github.com/antfu-collective/ni>.

- 모든 의존성 설치 (`npm install`, `yarn install` 등과 동일):

`ni`

- 특정 패키지 설치 (-D는 개발전용 의존성):

`ni {{패키지}}`

- `package.json` 스크립트 실행 (스크립트를 지정하지 않으면, 대화형으로 선택):

`nr {{스크립트}}`

- 패키지의 명령어를 다운로드하여 실행 (`npx`, `pnpm dlx` 등과 동일):

`nlx {{패키지}}`

- 의존성 업그레이드:

`nup`

- 패키지 제거:

`nun {{패키지}}`

- 의존성 클린 설치 (`npm ci` 등과 동일):

`nci`

- 현재 사용 중인 패키지 관리자를 직접 사용해, 임의의 명령 실행:

`na {{명령어}}`
