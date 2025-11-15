# tac

> 파일을 역순으로 표시하고 연결.
> 같이 보기: `cat`.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- 특정 파일들을 역순으로 연결:

`tac {{경로/대상/파일1 경로/대상/파일2 ...}}`

- `stdin`을 역순으로 표시:

`{{cat 경로/대상/파일}} | tac`

- 특정 [s]eparator 사용:

`tac -s {{구분자}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 특정 [r]egex를 [s]eparator로 사용:

`tac -r -s {{구분자}} {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 각 파일 앞에 구분자 [b]efore 사용:

`tac -b {{경로/대상/파일1 경로/대상/파일2 ...}}`
