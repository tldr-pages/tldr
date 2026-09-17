# tmt run

> `tmt` 테스트 단계를 실행. 기본값으로, 모든 테스트 단계를 실행.
> 더 많은 정보: <https://tmt.readthedocs.io/en/stable/stories/cli.html#run>.

- 각 계획에 대해 모든 테스트 단계 실행:

`tmt run`

- discover 단계만 실행하여 어떤 테스트가 실행될 지 확인:

`tmt run discover {{[-v|--verbose]}}`

- 모든 단계를 실행하면서 provision 단계 옵션 지정:

`tmt run {{[-a|--all]}} provision {{[-h|--how]}} {{컨테이너}} {{[-i|--image]}} {{fedora:rawhide}}`

- 특정 플랜과 테스트만 선택하여 실행:

`tmt run plan {{[-n|--name]}} {{/플랜/이름}} test {{[-n|--name]}} {{/테스트/이름}}`

- 마지막 실행 결과를 웹 브라우저로 표시:

`tmt run {{[-l|--last]}} report {{[-h|--how]}} {{html}} {{[-o|--open]}}`

- 지정한 컨텍스트로 테스트 실행:

`tmt run {{[-c|--context]}} {{key=value}} {{[-c|--context]}} {{distro=fedora}}`

- 대화형으로 테스트 실행 (테스트 중간에 디버깅 가능):

`tmt run {{[-a|--all]}} execute {{[-h|--how]}} {{tmt}} --interactive`

- dry 모드로 실행될 작업 확인 및 최대 상세정보 출력:

`tmt run {{[-n|--dry]}} {{[-vvv|--verbose --verbose --verbose]}}`
