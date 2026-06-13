# bun publish

> npm 레지스트리에 패키지를 배포.
> 더 많은 정보: <https://bun.com/docs/pm/cli/publish>.

- 현재 패키지를 npm 레지스트리에 배포:

`bun publish`

- 특정 디렉토리의 패키지 배포:

`bun publish {{경로/대상/패키지_디렉토리}}`

- scopeds 패키지를 특정 접근 권한으로 배포:

`bun publish --access {{public|restricted}}`

- 사용자 지정 레지스트리에 패키지 배포:

`bun publish --registry {{레지스트리}}`

- 실제 업로드 없이 배포 내용을 확인(dry run):

`bun publish --dry-run`

- 특정 distribution 태그로 배포:

`bun publish --tag {{태그_이름}}`

- 2FA 계정을 위한 일회용 비밀번호와 함께 배포:

`bun publish --otp {{one_time_password}}`

- 특정 인증 방식으로 배포:

`bun publish --auth-type {{web|legacy}}`
