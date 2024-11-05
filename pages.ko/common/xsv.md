# xsv

> Rust로 작성된 CSV 명령줄 도구 모음.
> 더 많은 정보: <https://github.com/BurntSushi/xsv>.

- 파일의 헤더 확인:

`xsv headers {{경로/대상/파일.csv}}`

- 항목 수 세기:

`xsv count {{경로/대상/파일.csv}}`

- 항목 형식 개요 보기:

`xsv stats {{경로/대상/파일.csv}} | xsv table`

- 몇몇 열 선택:

`xsv select {{열1,열2}} {{경로/대상/파일.csv}}`

- 10개의 무작위 항목 표시:

`xsv sample {{10}} {{경로/대상/파일.csv}}`

- 한 파일의 열을 다른 파일에 연결:

`xsv join --no-case {{열1}} {{경로/대상/파일1.csv}} {{열2}} {{경로/대상/파일2.csv}} | xsv table`
