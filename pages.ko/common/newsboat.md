# newsboat

> 텍스트 터미널용 RSS/Atom 피드 리더.
> 더 많은 정보: <https://newsboat.org/releases/2.40/docs/newsboat.html#_first_steps>.

- OPML 파일에서 피드 URL을 처음으로 가져오기:

`newsboat -i {{내-피드.xml}}`

- 또는 피드를 수동으로 추가:

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- Newsboat을 시작하고 시작 시 모든 피드를 새로 고침:

`newsboat -r`

- 비대화형 모드에서 하나 이상의 명령 실행:

`newsboat -x {{reload print-unread ...}}`

- 키보드 단축키 보기 (가장 관련 있는 것은 상태 줄에 표시됨):

`<?>`
