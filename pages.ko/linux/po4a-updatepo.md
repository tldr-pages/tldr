# po4a-updatepo

> 문서의 번역(PO 형식)을 업데이트합니다.
> 더 많은 정보: <https://po4a.org/man/man1/po4a-updatepo.1.php>.

- 원본 파일의 수정 사항에 따라 PO 파일 업데이트:

`po4a-updatepo --format {{text}} --master {{경로/대상/원본.txt}} --po {{경로/대상/결과물.po}}`

- 사용 가능한 형식 나열:

`po4a-updatepo --help-format`

- 원본 파일의 수정 사항에 따라 여러 PO 파일 업데이트:

`po4a-updatepo --format {{text}} --master {{경로/대상/원본.txt}} --po {{경로/대상/po1.po}} --po {{경로/대상/po2.po}}`
