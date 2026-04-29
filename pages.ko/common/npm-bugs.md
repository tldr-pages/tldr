# npm bugs

> 패키지의 버그를 웹 브라우저에서 보고할 수 있는 명령어.
> 패키지의 버그 트래커 URL 또는 지원 이메일을 자동으로 열기.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-bugs/>.

- 특정 패키지의 버그 트래커를 열어, 보고:

`npm bugs {{패키지_이름}}`

- `package.json` 파일 및 이름을 찾아 현재 패키지의 버그 트래커를 열기:

`npm bugs`

- `npm` 명령으로 URL을 열 때, 사용할 브라우저를 설정:

`npm {{[c|config]}} set browser {{브라우저_이름}}`

- URL 열기 방식 설정: `browser`를 `true`로 설정하면 시스템 기본 URL 실행기를 사용하고, `false`로 설정하면 URL을 터미널에 출력:

`npm {{[c|config]}} set browser {{true|false}}`
