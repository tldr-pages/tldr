# npm dist-tag

> 패키지의 배포 태그를 관리하는 명령어.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-dist-tag/>.

- 특정 패키지의 모든 배포 태그 목록 출력:

`npm dist-tag ls {{패키지_이름}}`

- 현재 패키지의 모든 배포 태그 목록 출력:

`npm dist-tag ls`

- 특정 패키지 버전에 배포 태그 추가:

`npm dist-tag add {{패키지_이름}}@{{버전}} {{태그}}`

- 패키지에서 배포 태그 제거:

`npm dist-tag rm {{패키지_이름}} {{태그}}`

- npm 설정에 지정된 기본 태그로 추가:

`npm dist-tag add {{패키지_이름}}@{{버전}}`

- 2단계 인증(OTP)을 사용해 태그 추가:

`npm dist-tag add {{패키지_이름}}@{{버전}} {{태그}} --otp {{일회용_비밀번호}}`
