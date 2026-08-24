# npm repo

> 패키지의 저장소 페이지를 브라우저에서 여는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-repo/>.

- 현재 프로젝트 (`package.json` 기준)의 저장소 페이지 열기:

`npm repo`

- 레지스트리 내 특정 패키지의 저장소 페이지 열기:

`npm repo {{패키지_이름}}`

- 여러 패키지의 저장소 페이지 한 번에 열기:

`npm repo {{패키지_이름1 패키지_이름2 ...}}`

- 브라우저를 열지 않고 저장소 URL 출력:

`npm repo --browser false`

- 특정 브라우저로 저장소 페이지 열기:

`npm repo --browser {{브라우저_이름}}`

- 특정 워크스페이스의 패키지 저장소 페이지 열기:

`npm repo --workspace {{워크스페이스_이름}}`
