# keepassxc-cli

> KeepassXC의 명령줄 인터페이스.
> 더 많은 정보: <https://manned.org/keepassxc-cli>.

- 항목 검색:

`keepassxc-cli search {{경로/대상/데이터베이스_파일}} {{이름}}`

- 폴더 내용 나열:

`keepassxc-cli ls {{경로/대상/데이터베이스_파일}} {{경로/대상/폴더}}`

- 자동 생성된 비밀번호로 항목 추가:

`keepassxc-cli add --generate {{경로/대상/데이터베이스_파일}} {{항목_이름}}`

- 항목 삭제:

`keepassxc-cli rm {{경로/대상/데이터베이스_파일}} {{항목_이름}}`

- 항목의 비밀번호를 클립보드에 복사:

`keepassxc-cli clip {{경로/대상/데이터베이스_파일}} {{항목_이름}}`

- TOTP 코드를 클립보드에 복사:

`keepassxc-cli clip --totp {{경로/대상/데이터베이스_파일}} {{항목_이름}}`

- 7개의 단어로 구성된 구문 생성:

`keepassxc-cli diceware --words {{7}}`

- 16개의 출력 가능한 ASCII 문자로 비밀번호 생성:

`keepassxc-cli generate --lower --upper --numeric --special --length {{16}}`
