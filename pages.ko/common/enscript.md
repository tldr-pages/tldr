# enscript

> 텍스트 파일을 PostScript, HTML, RTF, ANSI 및 겹쳐쓰기로 변환.
> 더 많은 정보: <https://manned.org/enscript>.

- 텍스트 파일에서 PostScript 파일:

`enscript {{경로/대상/입력_파일}} --output={{경로/대상/출력_파일}}`

- PostScript와 다른 언어로 파일을 생성:

`enscript {{경로/대상/입력_파일}} --language={{html|rtf|...}} --output={{경로/대상/출력_파일}}`

- 페이지를 열(최대 9개)로 분할하여 가로 레이아웃으로 PostScript 파일을 생성:

`enscript {{경로/대상/입력_파일}} --columns={{숫자}} --landscape --output={{경로/대상/출력_파일}}`

- 사용 가능한 구문 강조 언어 및 파일 형식 표시:

`enscript --help-highlight`

- 지정된 언어에 대한 구문 강조 및 색상을 사용하여 PostScript 파일을 생성:

`enscript {{경로/대상/입력_파일}} --color=1 --highlight={{언어}} --output={{경로/대상/출력_파일}}`
