# john

> 비밀번호 크래커.
> 더 많은 정보: <https://www.openwall.com/john/>.

- 비밀번호 해시 크래킹:

`john {{경로/대상/해시들.txt}}`

- 크래킹된 비밀번호 표시:

`john --show {{경로/대상/해시들.txt}}`

- 여러 파일에서 사용자 식별자로 크래킹된 비밀번호 표시:

`john --show --users={{사용자_ID들}} {{경로/대상/해시들1.txt 경로/대상/해시들2.txt ...}}`

- 사용자 정의 워드리스트를 사용하여 비밀번호 해시 크래킹:

`john --wordlist={{경로/대상/워드리스트.txt}} {{경로/대상/해시들.txt}}`

- 사용 가능한 해시 형식 나열:

`john --list=formats`

- 특정 해시 형식을 사용하여 비밀번호 해시 크래킹:

`john --format={{md5crypt}} {{경로/대상/해시들.txt}}`

- 단어 변형 규칙을 활성화하여 비밀번호 해시 크래킹:

`john --rules {{경로/대상/해시들.txt}}`

- 중단된 크래킹 세션을 상태 파일에서 복구, 예: `mycrack.rec`:

`john --restore={{경로/대상/mycrack.rec}}`
