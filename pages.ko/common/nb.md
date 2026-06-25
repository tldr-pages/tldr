# nb

> 노트 작성, 북마킹, 아카이빙을 위한 도구.
> 암호화, 태깅, 위키 스타일 링크, Git 동기화, Pandoc 변환 등을 지원
> 더 많은 정보: <https://github.com/xwmx/nb#-help>.

- `$EDITOR`에서 새로운 노트 생성:

`nb {{[a|add]}} "{{노트_제목}}"`

- `$EDITOR`에서 노트 수정:

`nb {{[e|edit]}} {{노트_아이디}}`

- 현재 노트북의 모든 노트 목록 출력:

`nb list`

- 할 일 추가:

`nb {{[to|todos]}} {{[a|add]}} {{제목}}`

- 파일 또는 URL 가져오기:

`nb import ({{경로/대상/파일|주소}})`

- 키워드로 노트 검색:

`nb {{[q|search]}} "{{키워드}}"`

- Git을 통해 노트 동기화:

`nb sync`

- 도움말 표시:

`nb help`
