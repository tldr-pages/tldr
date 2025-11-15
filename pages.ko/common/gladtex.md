# gladtex

> HTML 파일용 LaTeX 수식 전처리기.
> LaTeX 수식을 이미지로 변환.
> 더 많은 정보: <https://manned.org/gladtex.1>.

- HTML로 변환:

`gladtex {{경로/대상/입력파일.htex}}`

- 변환된 파일을 특정 위치에 저장:

`gladtex {{경로/대상/입력파일.htex}} -o {{경로/대상/출력파일.html}}`

- 생성된 이미지를 특정 디렉토리([d]irectory)에 저장:

`gladtex {{경로/대상/입력파일.htex}} -d {{경로/대상/이미지_출력_디렉토리}}`

- 이미지 해상도([r]esolution) 설정 (dpi 단위, 기본값은 100):

`gladtex {{경로/대상/입력파일.htex}} -r {{resolution}}`

- 변환 후 LaTeX 파일 유지([k]eep) :

`gladtex {{경로/대상/입력파일.htex}} -k`

- 이미지의 배경([b]ackground) 및 전경([f]oreground)색 설정:

`gladtex {{경로/대상/입력파일.htex}} -b {{배경_색}} -f {{전경_색}}`

- `pandoc` 및 `gladtex`를 사용하여 마크다운을 HTML로 변환:

`pandoc -s -t html --gladtex {{경로/대상/입력파일.md}} | gladtex -o {{경로/대상/출력파일.html}}`
