# gendesk

> 최소한의 정보로 `.desktop` 파일과 아이콘 다운로드 항목 생성.
> 더 많은 정보: <https://manned.org/gendesk>.

- `app`이라는 이름의 `.desktop` 파일 생성:

`gendesk -n --name "{{app}}" --exec "/{{경로/대상/애플리케이션}}" --icon "/{{경로/대상/아이콘.png}}" --comment "{{This is application}}"`

- 출력없이 기존 파일을 덮어쓰면서, `app`이라는 이름의 `.desktop` 파일 생성:

`gendesk -q -f -n --name "{{app}}" --exec "/{{경로/대상/애플리케이션}}" --icon "/{{경로/대상/아이콘.png}}" --comment "{{This is application}}"`

- 도움말 표시:

`gendesk {{[-h|--help]}}`
