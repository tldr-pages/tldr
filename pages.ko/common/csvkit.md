# csvkit

> CSV 파일용 조작 도구 모음.
> 참고: `csvclean`, `csvcut`, `csvformat`, `csvgrep`, `csvlook`, `csvpy`, `csvsort`, `csvstat`.
> 더 많은 정보: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>.

- 사용자 정의 구분 기호를 사용해 CSV 파일에 대해 명령을 실행:

`{{명령어}} -d {{구분자}} {{경로/대상/파일.csv}}`

- 탭을 구분 기호로 사용하여 CSV 파일에서 명령을 실행 (-d를 덮어씌움):

`{{명령어}} -t {{경로/대상/파일.csv}}`

- 사용자 정의 따옴표 문자를 사용하여 CSV 파일에서 명령을 실행:

`{{명령어}} -q {{따옴표_문자}} {{경로/대상/파일.csv}}`

- 헤더 행이 없는 CSV 파일에 대해 명령을 실행:

`{{명령어}} -H {{경로/대상/파일.csv}}`
