# mu

> 로컬 Maildir에서 이메일을 색인하고 검색.
> 더 많은 정보: <https://man.cx/mu>.

- 이메일 데이터베이스 초기화, 선택적으로 Maildir 디렉토리와 이메일 주소 지정:

`mu init --maildir={{경로/대상/폴더}} --my-address={{name@example.com}}`

- 새로운 이메일 색인:

`mu index`

- 특정 키워드를 사용하여 메시지 찾기 (메시지 본문, 제목, 발신자 등):

`mu find {{키워드}}`

- Alice에게 보낸 메시지 중 제목이 `jellyfish`이고 본문에 `apples` 또는 `oranges`가 포함된 메시지 찾기:

`mu find to:{{alice}} subject:{{jellyfish}} {{apples}} OR {{oranges}}`

- 보낸 편지함에 있는, `soc`로 시작하는 단어에 대한 읽지 않은 메시지 찾기 (`*`는 검색어 끝에서만 작동):

`mu find 'subject:{{soc}}*' flag:{{unread}} maildir:'/{{Sent Items}}'`

- Sam에게서 온, 이미지가 첨부된 2 KiB에서 2 MiB 사이의 크기로 2021년에 작성된 메시지 찾기:

`mu find 'mime:{{image/*}} size:{{2k..2m}} date:{{20210101..20211231}} from:{{sam}}`

- 이름 또는 이메일 주소에 `Bob`이 포함된 연락처 나열:

`mu cfind {{Bob}}`
