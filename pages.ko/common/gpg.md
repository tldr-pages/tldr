# gpg

> GNU Privacy Guard.
> GNU Privacy Guard 2에 대해서는 `gpg2`를 참조. 대부분의 운영체제는 `gpg`를 `gpg2`에 심볼릭 링크를 설정함.
> 더 많은 정보: <https://gnupg.org>.

- GPG 공개 및 개인 키를 대화형으로 생성:

`gpg --full-generate-key`

- 암호화 없이 `doc.txt`에 서명 (`doc.txt.asc`에 출력을 기록):

`gpg --clearsign {{doc.txt}}`

- alice@example.com 및 bob@example.com에 대해 `doc.txt`를 암호화하고 서명 (`doc.txt.gpg`로 출력):

`gpg --encrypt --sign --recipient {{alice@example.com}} --recipient {{bob@example.com}} {{doc.txt}}`

- 비밀번호 문구만으로 `doc.txt`를 암호화 (`doc.txt.gpg`로 출력):

`gpg --symmetric {{doc.txt}}`

- `doc.txt.gpg` 복호화 (`stdout`으로 출력):

`gpg --decrypt {{doc.txt.gpg}}`

- 공개 키 가져오기:

`gpg --import {{public.gpg}}`

- alice@example.com에 대한 공개 키 내보내기 (`stdout`으로 출력):

`gpg --export --armor {{alice@example.com}}`

- alice@example.com의 개인 키 내보내기 (`stdout`으로 출력):

`gpg --export-secret-keys --armor {{alice@example.com}}`
