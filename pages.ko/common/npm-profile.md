# npm profile

> npm 프로필과 관련 설정을 관리하는 명령어.
> 참고: 이 명령어는 workspaces를 지원하지 않음.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-profile/>.

- npm 프로필 정보 조회:

`npm profile get`

- 특정 프로필 속성 조회:

`npm profile get {{속성}}`

- Set or update a profile property:

`npm profile set {{속성}} {{값}}`

- 공개 이메일 주소 설정:

`npm profile set email {{이메일}}`

- 공개 이름 설정:

`npm profile set fullname {{이름}}`

- 새로운 비밀번호를 대화형으로 설정:

`npm profile set password`

- 2단계 인증(2FA) 활성화 (기본: `auth-and-writes`):

`npm profile enable-2fa {{auth-only|auth-and-writes}}`

- 2단계 인증(2FA) 비활성화:

`npm profile disable-2fa`
