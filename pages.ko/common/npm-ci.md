# npm ci

> 자동와 환경에서 사용하는 `npm` 프로젝트 의존성의 클린 설치 명령어.
> `package-lock.json` 또는 `npm-shrinkwrap.json` 기준으로 패키지를 설치.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-ci/>.

- `package-lock.json` 또는 `npm-shrinkwrap.json`을 기반으로 의존성 설치:

`npm ci`

- 특정 유형의 의존성을 제외하고 설치:

`npm ci --omit {{dev|optional|peer}}`

- `package.json`에 정의된 pre/post 스크립트를 실행하지 않고 설치:

`npm ci --ignore-scripts`
