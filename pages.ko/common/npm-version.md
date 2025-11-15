# npm version

> Node 패키지의 버전을 증가시킵니다.
> 더 많은 정보: <https://docs.npmjs.com/cli/npm-version>.

- 현재 버전 확인:

`npm version`

- 마이너 버전 증가:

`npm version minor`

- 특정 버전 설정:

`npm version {{버전}}`

- Git 태그를 생성하지 않고 패치 버전 증가:

`npm version patch --no-git-tag-version`

- 사용자 정의 커밋 메시지와 함께 메이저 버전 증가:

`npm version major -m "{{%s 이유로 업그레이드함}}"`
