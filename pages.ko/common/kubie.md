# kubie

> `kubectl` 컨텍스트와 네임스페이스를 전환하는 유틸리티.
> 더 많은 정보: <https://github.com/sbstp/kubie#usage>.

- 선택 가능한 컨텍스트 메뉴 표시:

`kubie ctx`

- 현재 쉘을 지정한 컨텍스트로 전환:

`kubie ctx {{컨텍스트}}`

- 현재 쉘을 지정한 네임스페이스로 전환:

`kubie ns {{네임스페이스}}`

- 현재 쉘을 지정한 컨텍스트와 네임스페이스로 전환:

`kubie ctx {{컨텍스트}} {{[-n|--namespace]}} {{네임스페이스}}`

- 쉘을 생성하지 않고, 지정한 컨텍스트와 네임스페이스에서 명령 실행:

`kubie exec {{컨텍스트}} {{네임스페이스}} {{명령어}}`

- Kubernetes 설정 파일 문제점 검사:

`kubie lint`
