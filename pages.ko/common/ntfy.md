# ntfy

> HTTP POST 알림을 보내고 받기.
> 더 많은 정보: <https://github.com/binwiederhier/ntfy>.

- `security` 토픽에 메시지 보내기:

`ntfy pub security "{{현관문이 열렸습니다.}}"`

- 제목, 우선순위 및 태그와 함께 보내기:

`ntfy publish --title="{{누군가 당신의 아이템을 구매했습니다}}" --priority={{높음}} --tags={{오리}} {{이베이}} "{{누군가 당신의 아이템을 구매했습니다: 오리너구리 조각상}}"`

- 오전 8시 30분에 보내기:

`ntfy pub --at=8:30am {{지연된_토픽}} "{{학교 갈 시간이야, 졸린이...}}"`

- 웹훅 트리거:

`ntfy trigger {{나의_웹훅}}`

- 토픽 구독하기 (`<Ctrl c>`로 듣기 중지):

`ntfy sub {{홈_자동화}}`

- 도움말 표시:

`ntfy --help`
