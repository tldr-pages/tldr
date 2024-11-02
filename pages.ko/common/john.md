# john

> 패스워드 크래커.
> 더 많은 정보: <https://www.openwall.com/john/>.

- 패스워드 해시 크랙:

`john {{경로/대상/해시목록.txt}}`

- 크랙된 패스워드 표시:

`john --show {{경로/대상/해시목록.txt}}`

- 여러 파일에서 사용자 식별자별로 크랙된 패스워드 표시:

`john --show --users={{사용자_IDs}} {{경로/대상/hashes1.txt 경로/대상/hashes2.txt ...}}`

- 사용자 정의 워드리스트를 사용하여 패스워드 해시 크랙:

`john --wordlist={{경로/대상/워드리스트.txt}} {{경로/대상/해시목록.txt}}`

- 사용 가능한 해시 형식 나열:

`john --list=formats`

- 특정 해시 형식을 사용하여 패스워드 해시 크랙:

`john --format={{md5crypt}} {{경로/대상/해시목록.txt}}`

- 단어 변형 규칙을 활성화하여 패스워드 해시 크랙:

`john --rules {{경로/대상/해시목록.txt}}`

- 예를 들어, `mycrack.rec`와 같은 상태 파일에서 중단된 크래킹 세션 복원:

`john --restore={{경로/대상/mycrack.rec}}`
