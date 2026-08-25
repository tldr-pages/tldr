# npm prune

> `node_modules`에서 불필요한 패키지를 제거하는 명령어.
> 참고: 불필요한 패키지는 어떤 패키지의 의존성 목록에도 포함되지 않은 패키지를 의미.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-prune/>.

- 의존성에 포함되지 않은 모든 불필요한 패키지 제거:

`npm prune`

- 불필요한 패키지와 devDependencies 제거 (프로덕션 빌드에 유용):

`npm prune --production`

- 실제 변경 없이 제거 대상 미리보기:

`npm prune --dry-run`

- 변경 내용을 JSON 형식으로 출력:

`npm prune --json`

- 특정 패키지 이름으로 제거:

`npm prune {{패키지_이름}}`
