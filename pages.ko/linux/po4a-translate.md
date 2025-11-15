# po4a-translate

> PO 파일을 문서 형식으로 다시 변환.
> 제공된 PO 파일은 `po4a-gettextize`로 생성된 POT 파일의 번역본이어야 합니다.
> 더 많은 정보: <https://po4a.org/man/man1/po4a-translate.1.php>.

- 번역된 PO 파일을 문서로 다시 변환:

`po4a-translate --format {{텍스트}} --master {{경로/대상/원본.doc}} --po {{경로/대상/결과.po}} --localized {{경로/대상/번역된.txt}}`

- 사용 가능한 모든 형식 나열:

`po4a-translate --help-format`
