# column

> 표준 입력 또는 파일을 여러 열로 포맷 설정.
> 행은 열 앞에 채워집니다; 기본 구분 기호는 공백입니다.

- 30자 폭 디스플레이의 형식 출력으로 포맷 정하기:

`printf "header1 header2\nbar foo\n" | column -c {{30}}`

- 열 자동 분할 및 자동 정렬을 표 형식으로 분할:

`printf "header1 header2\nbar foo\n" | column -t`

- -t 옵션(예: "", csv)에 대한 열 구분 기호 문자를 지정; 기본값은 공백입니다:

`printf "header1,header2\nbar,foo\n" | column -t -s{{,}}`

- 행을 채우기 전에 열을 채웁니다:

`printf "header1\nbar\nfoobar\n" | column -c {{30}} -x`
