# hashid

> 데이터 및 비밀번호 해시를 식별하는 Python3 프로그램.
> 더 많은 정보: <https://github.com/psypanda/hashID>.

- `stdin`에서 해시를 식별 (입력, 복사 및 붙여넣기 또는 해시를 프로그램에 파이프 사용):

`hashid`

- 하나 이상의 해시를 식별:

`hashid {{해시1 해시2 ...}}`

- 파일의 해시를 식별 (한 줄에 하나의 해시):

`hashid {{경로/대상/해시.txt}}`

- 가능한 모든 해시 유형 표시 (salt된 해시를 포함):

`hashid --extended {{해시}}`

- `hashcat`의 모드 번호와 `john`의 해시 유형 형식 문자열을 표시:

`hashid --mode --john {{해시}}`

- `stdout`으로 출력하는 대신 파일에 출력을 저장:

`hashid --outfile {{경로/대상/출력파일.txt}} {{해시}}`
