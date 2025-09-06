# cpdf

> PDF 파일 조작.
> 더 많은 정보: <https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>.

- 소스 문서에서 1, 2, 3 및 6페이지를 선택하고 이를 대상 문서에 작성:

`cpdf {{경로/대상/소스_문서.pdf}} {{1-3,6}} -o {{경로/대상/대상_문서.pdf}}`

- 두 개의 문서를 새 문서로 병합:

`cpdf -merge {{경로/대상/소스_문서_1.pdf}} {{경로/대상/소스_문서_2.pdf}} -o {{경로/대상/대상_문서.pdf}}`

- 문서의 북마크 표시:

`cpdf -list-bookmarks {{경로/대상/문서.pdf}}`

- 문서를 10페이지 단위로 나누어 `chunk001.pdf`, `chunk002.pdf` 등에 작성:

`cpdf -split {{경로/대상/문서.pdf}} -o {{경로/대상/문서%%%.pdf}} -chunk {{10}}`

- 128비트 암호화를 사용하여 문서를 암호화하고, `fred`를 소유자 비밀번호로, `joe`를 사용자 비밀번호로 제공:

`cpdf -encrypt {{128bit}} {{fred}} {{joe}} {{경로/대상/소스_문서.pdf}} -o {{경로/대상/암호화된_문서.pdf}}`

- 소유자 비밀번호 `fred`를 사용하여 문서를 해독:

`cpdf -decrypt {{경로/대상/암호화된_문서.pdf}} owner={{fred}} -o {{경로/대상/복호화된_문서.pdf}}`

- 문서의 주석 표시:

`cpdf -list-annotations {{경로/대상/문서.pdf}}`

- 추가 메타데이터를 사용하여 기존 문서에서 새 문서를 생성:

`cpdf -set-metadata {{경로/대상/메타데이터.xml}} {{경로/대상/소스_문서.pdf}} -o {{경로/대상/대상_문서.pdf}}`
