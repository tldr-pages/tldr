# bun remove

> `package.json`에서 의존성을 제거.
> 더 많은 정보: <https://bun.com/docs/pm/cli/remove>.

- 의존성 제거:

`bun {{[rm|remove]}} {{패키지_이름}}`

- 여러 의존성 제거:

`bun {{[rm|remove]}} {{패키지_이름1 패키지_이름2 ...}}`

- 전역으로 설치된 패키지 제거:

`bun {{[rm|remove]}} {{[-g|--global]}} {{패키지_이름}}`

- `package.json` 파일 업데이트 없이 의존성 제거:

`bun {{[rm|remove]}} --no-save {{패키지_이름}}`

- 실제로 제거하지 않고 명령어만 실행 (dry run):

`bun {{[rm|remove]}} --dry-run {{패키지_이름}}`
