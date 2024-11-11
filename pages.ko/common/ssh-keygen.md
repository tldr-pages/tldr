# ssh-keygen

> 인증, 비밀번호 없는 로그인 및 기타 용도로 사용되는 SSH 키 생성.
> 더 많은 정보: <https://man.openbsd.org/ssh-keygen>.

- 대화식으로 키 생성:

`ssh-keygen`

- 32 키 유도 함수 라운드로 ed25519 키를 생성하고 특정 파일에 키 저장:

`ssh-keygen -t {{ed25519}} -a {{32}} -f {{~/.ssh/파일_이름}}`

- 이메일을 주석으로 하는 4096비트 RSA 키 생성:

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{주석|이메일}}"`

- known_hosts 파일에서 호스트의 키 제거 (알려진 호스트가 새 키를 가지는 경우 유용):

`ssh-keygen -R {{원격_호스트}}`

- MD5 Hex로 키의 지문 검색:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/파일_이름}}`

- 키의 비밀번호 변경:

`ssh-keygen -p -f {{~/.ssh/파일_이름}}`

- 키 형식 변경 (예: OPENSSH 형식에서 PEM으로), 파일은 제자리에서 다시 작성됨:

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_개인_키}}`

- 비밀 키에서 공개 키 추출:

`ssh-keygen -y -f {{~/.ssh/OpenSSH_개인_키}}`
