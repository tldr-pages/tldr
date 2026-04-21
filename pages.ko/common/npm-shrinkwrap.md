# npm shrinkwrap

> 패키지의 의존성을 고정해, `npm-shrinkwrap.json` 파일을 생성하는 명령어.
> `package-lock.json`와 유사하지만 배포용 패키지에 사용됨.
> 더 많은 정보: <https://docs.npmjs.com/cli/shrinkwrap/>.

- 현재 `package-lock.json`을 기반으로 `npm-shrinkwrap.json` 생성:

`npm shrinkwrap`

- 프로덕션 모드로 실행 (devDependencies 제외):

`npm shrinkwrap --production`

- 이미 존재해도 강제로 shrinkwrap 파일 재생성:

`npm shrinkwrap --force`