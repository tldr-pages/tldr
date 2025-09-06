# iwctl

> `iwd` 네트워크 서플리컨트를 제어합니다.
> 더 많은 정보: <https://manned.org/iwctl>.

- 대화형 모드 시작, 이 모드에서는 자동 완성 기능과 함께 명령어를 직접 입력할 수 있습니다:

`iwctl`

- Wi-Fi 스테이션 표시:

`iwctl station list`

- 스테이션으로 네트워크 검색 시작:

`iwctl station {{스테이션}} scan`

- 스테이션에서 찾은 네트워크 표시:

`iwctl station {{스테이션}} get-networks`

- 스테이션으로 네트워크에 연결, 자격 증명이 필요할 경우 요청받습니다:

`iwctl station {{스테이션}} connect {{네트워크_이름}}`

- 일반 도움말 호출:

`iwctl {{[-h|--help]}}`
