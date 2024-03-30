# npm query

> CSS와 유사한 선택자를 사용하여 의존성 객체 배열을 출력합니다.
> 더 많은 정보: <https://docs.npmjs.com/cli/v8/commands/npm-query>.

- 직접 의존성 출력:

`npm query ':root > *'`

- 모든 직접 프로덕션/개발 의존성을 출력:

`npm query ':root > .{{prod|dev}}'`

- 특정 이름으로 의존성 출력:

`npm query '#{{패키지}}'`

- 특정 이름과 시맨틱 버전 관리 범위 내에서 의존성을 출력:

`npm query #{{패키지}}@{{시멘틱 버전}}`

- 의존성이 없는 의존성을 출력:

`npm query ':empty'`

- 설치 후 스크립트로 모든 의존성을 찾아 제거:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- 모든 Git 종속성을 찾아 어떤 애플리케이션에 필요한지 출력:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`
