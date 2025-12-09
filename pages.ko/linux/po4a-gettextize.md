# po4a-gettextize

> 파일을 PO 파일로 변환합니다.
> 더 많은 정보: <https://po4a.org/man/man1/po4a-gettextize.1.php>.

- 텍스트 파일을 PO 파일로 변환:

`po4a-gettextize --format {{text}} --master {{경로/대상/원본.txt}} --po {{경로/대상/결과.po}}`

- 사용 가능한 모든 형식 나열:

`po4a-gettextize --help-format`

- 번역된 문서와 함께 텍스트 파일을 PO 파일로 변환 (`-l` 옵션은 여러 번 제공할 수 있음):

`po4a-gettextize --format {{text}} --master {{경로/대상/원본.txt}} --localized {{경로/대상/번역된.txt}} --po {{경로/대상/결과.po}}`
