# gpg2

> GNU Privacy Guard 2.
> GNU Privacy Guard 1에 대해서는 `gpg`를 참조.
> 더 많은 정보: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- 가져온 키 목록 나열:

`gpg2 --list-keys`

- 지정된 수신자에 대해 지정된 파일을 암호화하고, `.gpg`가 추가된 새로운 파일에 출력을 작성:

`gpg2 --encrypt --recipient {{alice@example.com}} {{경로/대상/문서.txt}}`

- 암호만 사용하여 지정된 파일을 암호화하고, `.gpg`가 추가된 새로운 파일에 출력을 작성:

`gpg2 --symmetric {{경로/대상/문서.txt}}`

- 지정된 파일의 암호를 복호화하고, 결과를 `stdout`에 기록:

`gpg2 --decrypt {{경로/대상/문서.txt.gpg}}`

- 공개 키 가져오기:

`gpg2 --import {{경로/대상/공개_키.gpg}}`

- 지정된 이메일 주소의 공개 키를 `stdout`으로 내보내기 :

`gpg2 --export --armor {{alice@example.com}}`

- 지정된 이메일 주소가 포함된 개인 키를 `stdout`으로 내보내기:

`gpg2 --export-secret-keys --armor {{alice@example.com}}`
