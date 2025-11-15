# notmuch

> 대량의 이메일 메시지를 색인화, 검색, 읽기 및 태깅하기 위한 명령줄 기반 프로그램.
> 더 많은 정보: <https://notmuchmail.org/manpages/>.

- 초기 사용을 위한 설정:

`notmuch setup`

- 검색어와 일치하는 모든 메시지에 태그 추가:

`notmuch tag +{{사용자_정의_태그}} "{{검색_어구}}"`

- 검색어와 일치하는 모든 메시지의 태그 제거:

`notmuch tag -{{사용자_정의_태그}} "{{검색_어구}}"`

- 주어진 검색어와 일치하는 메시지 수 세기:

`notmuch count --output={{messages|threads}} "{{검색_어구}}"`

- 주어진 검색어와 일치하는 메시지 검색:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} "{{검색_어구}}"`

- 검색 결과를 X개로 제한:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} --limit={{X}} "{{검색_어구}}"`

- 메시지 세트에 대한 회신 템플릿 생성:

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} "{{검색_어구}}"`
